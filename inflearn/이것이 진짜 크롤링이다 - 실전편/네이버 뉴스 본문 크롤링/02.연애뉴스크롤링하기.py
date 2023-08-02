import requests
from bs4 import BeautifulSoup
import time

response = requests.get('https://search.naver.com/search.naver?sm=tab_sug.top&where=news&query=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC&oquery=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&tqi=iKA3Osp0Jy0ssAOUMeRssssssp8-023457&acq=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC&acr=2&qdt=0')
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
        # print(url)
        # 만약 연예 뉴스 라면
        if 'entertain' in response.url:
            title = soup.select_one('.end_tit')
            content = soup.select_one('#articeBody')
        else:
            title = soup.select_one('#title_area')
            content = soup.select_one('#dic_area')
    
        print("==========링크==========\n", url)
        print("==========제목==========\n", title.text.strip())
        print("==========내용==========\n", content.text.strip())
    
        time.sleep(0.3)