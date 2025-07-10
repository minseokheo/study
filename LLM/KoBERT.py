import pandas as pd
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AdamW, get_linear_schedule_with_warmup
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# --- 1. 설정 및 전역 변수 ---
MODEL_PATH = './kobert-from-skt' # 2번 단계에서 다운로드한 로컬 폴더 경로
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MAX_LEN = 128
BATCH_SIZE = 8
EPOCHS = 5
LEARNING_RATE = 2e-5

# --- 2. 데이터 로드 및 전처리 ---
print("Step 1: 데이터 로딩 및 전처리 시작")
df = pd.read_csv("kobert_multilabel_sample.csv")

# 입력(X)과 타겟(y) 분리
# '문서제목'과 '기안한부서'를 [SEP] 토큰으로 연결하여 하나의 입력으로 만듦
df['combined_text'] = df['문서제목'] + ' [SEP] ' + df['기안한부서']
X = df['combined_text'].values

# '배부될부서'를 리스트 형태로 변환
y_raw = [str(label).split(';') for label in df['배부될부서']]

# MultiLabelBinarizer를 사용하여 y를 원-핫 인코딩 벡터로 변환
mlb = MultiLabelBinarizer()
y = mlb.fit_transform(y_raw)
num_labels = len(mlb.classes_)

# MultiLabelBinarizer 객체 저장 (나중에 예측 결과를 부서명으로 변환할 때 필요)
with open('mlb.pkl', 'wb') as f:
    pickle.dump(mlb, f)

print(f"총 {num_labels}개의 부서 레이블 발견: {mlb.classes_}")

# 데이터셋 분할
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
print("데이터 분할 완료: Train {len(X_train)}, Validation {len(X_val)}")

# --- 3. 토크나이저 및 PyTorch Dataset 생성 ---
print("\nStep 2: 토크나이저 및 Dataset 생성")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

class CustomDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = str(self.texts[idx])
        label = torch.tensor(self.labels[idx], dtype=torch.float32) # BCEWithLogitsLoss는 float 타입을 요구

        encoding = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=self.max_len,
            return_token_type_ids=False,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt',
        )

        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': label
        }

train_dataset = CustomDataset(X_train, y_train, tokenizer, MAX_LEN)
val_dataset = CustomDataset(X_val, y_val, tokenizer, MAX_LEN)

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE)

# --- 4. 모델 로드 및 학습 설정 ---
print("\nStep 3: 모델 로드 및 학습 설정")
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_PATH,
    num_labels=num_labels,
    problem_type="multi_label_classification" # ⭐ 핵심: 다중 레이블 분류 문제임을 명시
).to(DEVICE)

# 옵티마이저와 스케줄러 설정
optimizer = AdamW(model.parameters(), lr=LEARNING_RATE, eps=1e-8)
total_steps = len(train_loader) * EPOCHS
scheduler = get_linear_schedule_with_warmup(
    optimizer,
    num_warmup_steps=0,
    num_training_steps=total_steps
)

# --- 5. 모델 학습 ---
print("\nStep 4: 모델 학습 시작")
for epoch in range(EPOCHS):
    model.train()
    total_loss = 0
    for batch in train_loader:
        optimizer.zero_grad()
        
        input_ids = batch['input_ids'].to(DEVICE)
        attention_mask = batch['attention_mask'].to(DEVICE)
        labels = batch['labels'].to(DEVICE)

        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        total_loss += loss.item()

        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        scheduler.step()

    avg_train_loss = total_loss / len(train_loader)
    print(f"Epoch {epoch + 1}/{EPOCHS} | Train Loss: {avg_train_loss:.4f}")


# --- 6. 모델 평가 ---
print("\nStep 5: 모델 평가 시작")
model.eval()
all_preds = []
all_labels = []

with torch.no_grad():
    for batch in val_loader:
        input_ids = batch['input_ids'].to(DEVICE)
        attention_mask = batch['attention_mask'].to(DEVICE)
        labels = batch['labels'].to(DEVICE)

        outputs = model(input_ids, attention_mask=attention_mask)
        
        # 로짓에 시그모이드 함수를 적용하고, 임계값(0.5)을 기준으로 0 또는 1로 변환
        logits = outputs.logits
        preds = torch.sigmoid(logits) > 0.5
        
        all_preds.extend(preds.cpu().numpy())
        all_labels.extend(labels.cpu().numpy())

# 리스트를 numpy 배열로 변환
all_preds = np.array(all_preds)
all_labels = np.array(all_labels)

# --- 7. 평가지표 계산 및 출력 ---
print("\n--- 최종 성능 평가 결과 ---")

# 다중 레이블 평가지표 계산 시 'average' 파라미터가 중요
# 'micro': 모든 레이블의 TP, FP, FN을 합산하여 계산. 클래스 불균형에 강건함.
# 'macro': 각 레이블별 지표를 계산 후 평균. 모든 클래스를 동일한 가중치로 취급.
# 'weighted': 각 레이블별 지표를 계산 후 클래스별 샘플 수에 따라 가중 평균.

eval_metrics = {
    'Accuracy (Exact Match Ratio)': accuracy_score(all_labels, all_preds),
    'F1 Score (Micro)': f1_score(all_labels, all_preds, average='micro', zero_division=0),
    'Precision (Micro)': precision_score(all_labels, all_preds, average='micro', zero_division=0),
    'Recall (Micro)': recall_score(all_labels, all_preds, average='micro', zero_division=0),
    'F1 Score (Macro)': f1_score(all_labels, all_preds, average='macro', zero_division=0),
    'Precision (Macro)': precision_score(all_labels, all_preds, average='macro', zero_division=0),
    'Recall (Macro)': recall_score(all_labels, all_preds, average='macro', zero_division=0),
    'F1 Score (Weighted)': f1_score(all_labels, all_preds, average='weighted', zero_division=0),
}

for name, value in eval_metrics.items():
    print(f"{name}: {value:.4f}")

# --- 8. 결과 시각화 ---
metric_names = ['F1 (Micro)', 'F1 (Macro)', 'F1 (Weighted)']
metric_values = [eval_metrics['F1 Score (Micro)'], eval_metrics['F1 Score (Macro)'], eval_metrics['F1 Score (Weighted)']]

plt.figure(figsize=(10, 6))
sns.barplot(x=metric_names, y=metric_values, palette='viridis')
plt.title('Multi-label Classification F1 Scores', fontsize=16)
plt.ylabel('Score', fontsize=12)
plt.ylim(0, 1)

# 막대 위에 값 표시
for index, value in enumerate(metric_values):
    plt.text(index, value + 0.01, f"{value:.3f}", ha='center', fontsize=11)

# 한글 폰트 설정 (환경에 맞는 폰트 경로 지정 필요)
# plt.rcParams['font.family'] = 'Malgun Gothic' # Windows
# plt.rcParams['axes.unicode_minus'] = False 
plt.show()

# --- 9. 모델 저장 (필요 시) ---
model.save_pretrained("./my_finetuned_kobert_model")
tokenizer.save_pretrained("./my_finetuned_kobert_model")
print("\n파인튜닝된 모델과 토크나이저가 './my_finetuned_kobert_model' 폴더에 저장되었습니다.")