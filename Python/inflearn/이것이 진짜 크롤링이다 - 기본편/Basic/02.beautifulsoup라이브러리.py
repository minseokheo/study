import requests
from bs4 import BeautifulSoup

# naver 서버에 대화를 시도
response = requests.get("http://www.naver.com/")

# naver 에서 html 줌
html = response.text

# html 번역선생님으로 수프 만듦
soup = BeautifulSoup(html, 'html.parser')

# id 값이 ke_kbd_btn인 놈 한개를 찾아냄
word = soup.select_one('#ke_kbd_btn')

# 텍스트 요소만 출력
print(word.text)