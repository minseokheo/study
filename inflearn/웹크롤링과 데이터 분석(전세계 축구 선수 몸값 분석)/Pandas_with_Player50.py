import pandas as pd

df1 = pd.DataFrame(
    {"이름" : ["손흥민", "메시", "호날두"],
     "나이" : [28, 33, 35],
     "소속" : ["토트넘", "바르셀로나", "유벤투스"]}
)
print(df1)

df1 = pd.DataFrame(
    {"이름" : ["손흥민", "메시", "호날두"],
     "나이" : [28, 33, 35],
     "소속" : ["토트넘", "바르셀로나", "유벤투스"]},
     index= [1, 2, 3]
)
print(df1)

player_list = [
    ['손흥민', 28, '토트넘'],
    ['메시', 33, '바르셀로나'],
    ['호날두', 35, '유벤투스']
]
df2 = pd.DataFrame(player_list, columns=['이름', '나이', '소속'])
print(df2)

# 필요한 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# requests.get()으로 url정보 요청하기
headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

player_list = []

for i in range(1, 3):
    url = f"https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop?ajax=yw1&page={i}"

    r = requests.get(url, headers=headers)
    # print(r.status_code)

    soup = BeautifulSoup(r.content, 'html.parser') # r.content 대신 r.text도 가능

    player_info = soup.find_all('tr', class_=['odd', 'even'])

    # player_info에서 'td'태그만 모두 찾기
    for info in player_info:
        player = info.find_all("td")

        number = player[0].text
        name = player[3].text
        position = player[4].text
        age = player[5].text
        nation = player[6].img['alt']
        team = player[7].img['alt']
        value = player[8].text.strip()
        # value = value[1:-1]
        # print(value)
        
        player_list.append([number, name, position, age, nation, team, value])

    time.sleep(1)

# pd.DataFrame()으로 저장하기
df2 = pd.DataFrame(player_list, columns=['number', 'name', 'position', 'age', 'nation', 'team', 'value'])
print(df2)

# df.to_csv()로 csv파일로 저장하기
df2.to_csv(r'C:\Users\tig06\Desktop\study\study\inflearn\웹크롤링과 데이터 분석(전세계 축구 선수 몸값 분석)\transfermarkt50.csv', index=False)