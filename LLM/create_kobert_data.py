import pandas as pd
import random

# 1. 샘플 데이터 정의
doc_titles = [
    "2025년 상반기 신입사원 채용 계획(안)", "영업1팀 워크샵 비용 정산 요청", "마케팅 전략 회의록 (7월 1주차)",
    "서버실 이전 작업에 따른 서비스 중단 안내", "법무 검토 요청: 신규 서비스 이용 약관", "2분기 재무 성과 보고",
    "인사평가 시스템 개선을 위한 TF팀 구성", "고객 클레임 처리 절차 변경 안내", "개발팀 신규 노트북 구매 품의",
    "사내 보안 강화 교육 실시 안내", "하반기 광고 예산 집행 계획", "경쟁사 동향 분석 보고서",
    "대표이사 주관 분기 실적 발표회 준비", "회계감사 대비 자료 준비 요청", "사내 동호회 지원금 신청"
]

origin_departments = [
    "인사총무팀", "영업1팀", "마케팅팀", "IT인프라팀", "법무팀", "재무회계팀",
    "인사총무팀", "고객지원팀", "개발1팀", "정보보안팀", "마케팅팀", "전략기획팀",
    "경영지원실", "재무회계팀", "인사총무팀"
]

# 2. 배부될 부서 목록 (총 73개라고 가정, 여기서는 10개로 축소하여 예시 생성)
all_departments = [
    "인사총무팀", "재무회계팀", "영업1팀", "영업2팀", "마케팅팀",
    "IT인프라팀", "개발1팀", "개발2팀", "법무팀", "경영지원실"
]

# 3. 데이터 생성
data = []
for i in range(len(doc_titles)):
    # 배부될 부서를 1~3개 랜덤으로 선택
    num_labels = random.randint(1, 3)
    target_depts = random.sample(all_departments, num_labels)
    
    data.append({
        "문서제목": doc_titles[i],
        "기안한부서": origin_departments[i],
        "배부될부서": ";".join(target_depts) # 세미콜론으로 다중 레이블 구분
    })

# 4. DataFrame 생성 및 CSV 파일로 저장
df = pd.DataFrame(data)
df.to_csv("kobert_multilabel_sample.csv", index=False, encoding='utf-8-sig')

print("샘플 데이터 파일 'kobert_multilabel_sample.csv' 생성이 완료되었습니다.")
print(df.head())