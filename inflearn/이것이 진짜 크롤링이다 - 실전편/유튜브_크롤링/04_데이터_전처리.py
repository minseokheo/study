from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pyautogui
import openpyxl

def text_to_num(text):
    text = text.replace("조회수", "").replace("회", "").strip()

    if "억" in text:
        num = float(text.replace("억", "")) * 100000000
    elif "만" in text:
        num = float(text.replace("만", "")) * 10000
    elif "천" in text:
        num = float(text.replace("천", "")) * 1000
    elif "없음" == text:
        num = 0
    else:
        num = int(text)
    
    return num

# 검색어 입력
keyword = pyautogui.prompt("검색어를 입력하세요")

# 엑셀 생성
wb = openpyxl.Workbook()
ws = wb.create_sheet(keyword)
ws.append(['번호', '제목', '조회수', '날짜'])

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

url = f"https://www.youtube.com/results?search_query={keyword}"

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

for i, info in enumerate(infos, 1):
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
    
    views = text_to_num(views)
    print(title, views, date)
    ws.append([i, title, views, date])

wb.save(f"C:/Users/tig06/OneDrive/Desktop/study/inflearn/이것이 진짜 크롤링이다 - 실전편/유튜브_크롤링/{keyword}.xlsx")
