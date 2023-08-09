import requests
from bs4 import BeautifulSoup

main_url = "https://www.coupang.com/np/search?component=&q=%EA%B2%8C%EC%9D%B4%EB%B0%8D+%EB%A7%88%EC%9A%B0%EC%8A%A4&channel=user"

# 헤더에 User-Agent를 추가하지 않으면 오류가 나요 (멈춰버림)
headers = {
    'Host': 'www.coupang.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
}
response = requests.get(main_url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

links = soup.select('a.search-product-link') # select의 결과는 리스트 자료형
print(links)