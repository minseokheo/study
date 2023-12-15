from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.youtube.com/results?search_query=%EC%A3%BC%EC%8B%9D"

browser.implicitly_wait(10)
browser.maximize_window()
browser.get(url)

# 7번 스크롤하기
scroll_count = 7

i = 1
while True:
    # 맨 아래로 스크롤을 내린다.
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    # 스크롤 사이에 페이지 로딩 시간
    time.sleep(2)

    if i == scroll_count:
        break
    i += 1

# Selenium - Beautifulsoup 연동방법
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
infos = soup.select(".text-wrapper")

for info in infos:
    # 원하는 정보 가져오기
    # 제목
    title = info.select_one("a#video-title").text

    try:
        # 조회수
        views = info.select_one("div#metadata-line > span:nth-of-type(1)").text

        # 날짜
        date = info.select_one("div#metadata-line > span:nth-of-type(2)").text
    except:
        views = "조회수 0회"
        date = "날짜 없음"
        
    print(title, views, date)