import requests
from bs4 import BeautifulSoup
import time

response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90')
# print(response)
html = response.text
# print(html)
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
articles = soup.select('div.info_group') # 뉴스 기사 div 10개 추출
# print(articles) # 리스트 형태로 출력

for article in articles:
    links = article.select('a.info') # 리스트
    if len(links) >= 2: # 링크가 2개 이상이면
        url = links[1].attrs['href'] # 두번째 링크의 href를 추출
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        content = soup.select_one('#dic_area')
        print(content.text)
        time.sleep(0.3)