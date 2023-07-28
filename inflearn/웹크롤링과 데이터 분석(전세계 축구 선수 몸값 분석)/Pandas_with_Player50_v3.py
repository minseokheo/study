import pandas as pd

# print()를 씌우면 출력가능

df = pd.read_csv(r'C:\Users\tig06\Desktop\study\study\inflearn\웹크롤링과 데이터 분석(전세계 축구 선수 몸값 분석)\transfermarkt50.csv')

# 칼럼 이름 바꾸고 저장하기 : 'team'을 'club'으로 바꾸기위해 cheat sheet에서 검색
df.rename(columns={'team':'club'}, inplace=True)

# 데이터 전처리(pre-processing)

# value 값에서 불필요한 문자를 없애고 데이터 타입을 숫자형으로 바꾸기
df['value'] = df['value'].str.replace('€', '')
df['value'] = df['value'].str.replace('m', '').astype('float')

# 칼럼 생성과 삭제

# 시장가치는 단위가 백만유로인데... 13을 곱해 한화로 억원으로 만들어줍니다.
df['시장가치(억)'] = df['value']*13

# 칼럼 삭제 df.drop(columns=['칼럼이름']) / inplace = True로 해야 저장됨
df.drop(columns=['value'], inplace=True)

# DataFrame 통계분석과 groupby()
# 숫자형 데이터에 대한 통계
df.describe()

# df[칼럼이름].mean()
# 나이 평균 구하기
df['age'].mean()

# 몸값 합계 구하기 sum()
df['시장가치(억)'].sum()

# 선수들이 속한 가장 많은 나라는? 최빈값 mode()
df['nation'].mode()

# 국적이 Brazil인 선수들은?
df[df['nation'] == 'England']

# groupby()

# 데이터를 그룹으로 묶어 분석
g = df.groupby('nation')
g.size()

# 수치형 데이터 총합 알아보기
# g.sum()

# 나라별 시장가치 총합
g['시장가치(억)'].sum()

# 선수들의 몸값의 합이 큰 클럽별로 정렬해서 보여주기
c = df.groupby("club")
print(c['시장가치(억)'].sum().sort_values(ascending=False))
