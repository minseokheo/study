import requests
from bs4 import BeautifulSoup

main_url = "https://www.coupang.com/np/search?component=&q=%EA%B2%8C%EC%9D%B4%EB%B0%8D+%EB%A7%88%EC%9A%B0%EC%8A%A4&channel=user"

# 헤더에 User-Agent를 추가하지 않으면 오류가 나요 (멈춰버림)
response = requests.get(main_url, headers={'User-Agent': 'Mozila/5.0'})
html = response.text
soup = BeautifulSoup(html, 'html.parser')

links = soup.select('a.search-product-link') # select의 결과는 리스트 자료형
print(links)