from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import urllib.request
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요 >>>")

if not os.path.exists(f'inflearn/이것이 진짜 크롤링이다 - 실전편/네이버 이미지 크롤링/{keyword}'):
    os.mkdir(f'inflearn/이것이 진짜 크롤링이다 - 실전편/네이버 이미지 크롤링/{keyword}')

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

url = f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}"
driver.get(url)

# 무한 스크롤 처리
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

# 이미지 태그 추출
imgs = driver.find_elements(By.CSS_SELECTOR, "._fe_image_tab_content_thumbnail_image")

for i, img in enumerate(imgs, 1):
    # 각 이미지 태그의 주소
    img_src = img.get_attribute("src")
    print(i, img_src)
    urllib.request.urlretrieve(img_src, f'inflearn/이것이 진짜 크롤링이다 - 실전편/네이버 이미지 크롤링/{keyword}/{i}.png')