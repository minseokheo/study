from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip
import csv

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5) # 웹 페이지가 로딩 될때까지 5초는 기다림
driver.maximize_window() # 화면 최대화
driver.get("https://shopping.naver.com/home")

# 검색창 클릭
search = driver.find_element(By.CSS_SELECTOR,"input._searchInput_search_text_3CUDs")
search.click()

# 검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = driver.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    # 맨 아래로 스크롤을 내린다.
    driver.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = driver.execute_script("return window.scrollY")

    if after_h == before_h:
        break

    before_h = after_h

# 파일 생성
f = open(r"C:\Users\tig06\OneDrive\Desktop\BOJ\study\inflearn\이것이 진짜 크롤링이다 - 기본편\03_네이버_쇼핑_크롤링\data.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)
# 상품 정보 div
items = driver.find_elements(By.CSS_SELECTOR,".product_inner__gr8QR")

for item in items:
    name = item.find_element(By.CSS_SELECTOR, ".product_title__Mmw2K").text
    try:
        price = item.find_element(By.CSS_SELECTOR, ".price_num__S2p_v").text
    except:
        price = "판매중단"
    link = item.find_element(By.CSS_SELECTOR, ".product_title__Mmw2K > a").get_attribute('href')
    print(name, price, link)
    
    # 데이터 쓰기
    csvWriter.writerow([name, price, link])

# 파일 닫기
f.close()