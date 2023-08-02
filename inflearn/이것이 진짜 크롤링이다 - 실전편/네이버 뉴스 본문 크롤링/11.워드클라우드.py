import requests
from bs4 import BeautifulSoup
import time
import pyautogui
import pyperclip

# 사용자입력
keyword = pyautogui.prompt('검색어를 입력하세요')
lastpage = int(pyautogui.prompt('몇 페이지까지 크롤링 할까요?'))

# 본문 전체 내용
total_content = ""

# 기사 개수
article_num = 0

page_num = 1
for i in range(1, lastpage * 10, 10):
    print(f"{page_num}페이지 크롤링 중입니다.===========================")
    response = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}')
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
            # 만약 스포츠 뉴스 라면
            if 'sports' in response.url:
                content = soup.select_one('#newsEndContents')
                # 본문 내용안에 불필요한 div, p 삭제
                divs = content.select('div')
                for div in divs:
                    div.decompose()
                paragraphs = content.select('p')
                for p in paragraphs:
                    p.decompose()
            # 만약 연예 뉴스 라면
            elif 'entertain' in response.url:
                content = soup.select_one('#articeBody')
            else:
                content = soup.select_one('#dic_area')

            print("==========본문==========\n", content.text.strip())
            total_content += content.text.strip()
            article_num = article_num + 1
            time.sleep(0.3)
    page_num = page_num + 1

print(f'{article_num}개 기사 크롤링 완료!!!')

# 클립보드에 복사하는 코드
pyperclip.copy(total_content)
pyautogui.alert('클립보드에 복사되었습니다.')

# 클립보드에 복사가 되면 
# 잡코리아 글자수 세기에 붙여넣고 10만자가 되지 않게 조절 해 준 다음 
# 다시 복사하여 worditout이라는 사이트에 들어가서 붙여 넣고 시각화 할 수 있음