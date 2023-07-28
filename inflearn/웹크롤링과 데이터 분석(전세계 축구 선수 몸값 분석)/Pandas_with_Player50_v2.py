import pandas as pd

df = pd.read_csv(r'C:\Users\tig06\Desktop\study\study\inflearn\웹크롤링과 데이터 분석(전세계 축구 선수 몸값 분석)\transfermarkt50.csv')
print(df.shape)

(rows, columns) = df.shape

print(df.info())

print(df.head()) # 앞에서 5개만 출력
print(df.tail()) # 뒤에서 5개만 출력

# head에 숫자 삽입
print(df.head(3)) # 앞에서 3개만 출력
print(df.tail(7)) # 뒤에서 7개만 출력

# df[:] 인덱싱
print(df[0:5]) # = df.head()
print(df[10:16])

# 칼럼 이름 선택하기 df['칼럼이름']
# 'name'만 가져와서 처음 5개만 보여주기
print(df['name'].head())

# 여러 개 컬럼 이름 선택하기 - df[]안에 리스트로 삽입
# 'number', 'name', 'namtion' 정보를 보여주기
print(df[['name', 'number', 'nation']].head())

# 위 데이터에서 15번째부터 20번째까지 데이터 보여주기
print(df[15:21])

# iloc와 loc 실습
print(df.iloc[0:2]) # = print(df[0:2])

# loc는 인덱스 숫자(문자)를 기준으로한다. 즉, 마지막 숫자(문자)도 포함
print(df.loc[0:2])

# 쉼표를 기준으로 행과 열 표시 df.loc[행이름, 열이름]
# 첫번째 행의, 이름이 'name'인 값
print(df.loc[0, 'name'])

# 행은 처음부터 5까지, 열은 'name', 'team', 'value'인 값
print(df.loc[0:5, ['name', 'team', 'value']])

# 조건 인덱싱
print(df['age']<20)

# 조건 색인
print(df[df['age']<20])

# 소속팀이 토트넘인 선수
print(df[df['team'] == 'Tottenham Hotspur'])

# 나이가 30이상인 선수의 'name'과 'value'를 가져오세요
print(df.loc[df['age'] >= 30, ['name', 'value']])

# 인덱스로 정리하기 df.sort_index()
print(df.sort_index().head())

# 내림차순으로 정리하기 (ascending = False)
print(df.sort_index(ascending=False)[:5])

# sort_values로 정렬하기 df.sort_values(칼럼이름)
# 나이 많은 선수 10명 보여주기
print(df.sort_values("age", ascending=False)[:10])

# 인덱스를 칼럼 이름으로 바꾸기 df.set_index("칼럼이름")
# number로 인덱스 바꿔보기
print(df.set_index('number').head())

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

print(df.head())