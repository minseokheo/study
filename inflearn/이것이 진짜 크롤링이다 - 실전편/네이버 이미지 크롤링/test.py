from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pyautogui
import os

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
keyword = pyautogui.prompt("검색어를 입력하세요")
driver.implicitly_wait(5) # 웹 페이지가 로딩 될때까지 5초는 기다림
driver.maximize_window() # 화면 최대화
driver.get(f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}")

os.mkdir('inflearn/이것이 진짜 크롤링이다 - 실전편/네이버 이미지 크롤링/' + keyword)