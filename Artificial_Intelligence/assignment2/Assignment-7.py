from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding
from keras import preprocessing
from keras.callbacks import EarlyStopping
from sklearn.model_selection import KFold
import numpy as np

dic_siz = 10000  # 사전의 크기(사전에 있는 단어 개수)
sample_siz = 512  # 샘플의 크기
k = 3  # 교차 검증 폴드 수

# tensorflow가 제공하는 간소한 버전의 IMDB 읽기
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=dic_siz)

embed_space_dim = 16  # 16차원의 임베딩 공간

x_train = preprocessing.sequence.pad_sequences(x_train, maxlen=sample_siz)
x_test = preprocessing.sequence.pad_sequences(x_test, maxlen=sample_siz)

early = EarlyStopping(monitor='val_accuracy', patience=5, restore_best_weights=True)

# KFold 객체를 생성하여 교차 검증용 인덱스를 생성
kf = KFold(n_splits=k, shuffle=True)

acc_scores = []

# 교차 검증 실행
for fold, (train_indices, val_indices) in enumerate(kf.split(x_train)):
    # 훈련 세트 준비
    x_tr = x_train[train_indices]
    y_tr = y_train[train_indices]

    # 검증 세트 준비
    x_val = x_train[val_indices]
    y_val = y_train[val_indices]

    # 신경망 모델의 설계와 학습(LSTM 층 포함)
    embed = Sequential()
    embed.add(Embedding(input_dim=dic_siz, output_dim=embed_space_dim, input_length=sample_siz))
    embed.add(LSTM(units=32))
    embed.add(Dense(1, activation='sigmoid'))
    embed.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])
    hist = embed.fit(x_tr, y_tr, epochs=5, batch_size=64, validation_data=(x_val, y_val), verbose=2, callbacks=[early])

    # 모델 평가
    res = embed.evaluate(x_test, y_test, verbose=0)
    acc_scores.append(res[1])

# 교차 검증 결과 출력
avg_acc = np.mean(acc_scores)
print("교차 검증 정확률:", avg_acc * 100)