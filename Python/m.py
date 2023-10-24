from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

browser.maximize_window() # 화면 최대화
# 초기 웹 페이지 열기
browser.get(f'https://sugang.knu.ac.kr')

# 학번 입력창
sid = browser.find_element(By.CSS_SELECTOR, "#stdno")
sid.click()
pyperclip.copy("") # 학번 입력
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# 아이디 입력창
id = browser.find_element(By.CSS_SELECTOR, "#userId")
id.click()
pyperclip.copy("") # 아이디 입력
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# 비밀번호 입력창
pw = browser.find_element(By.CSS_SELECTOR, "#pssrd")
pw.click()
pyperclip.copy("") # 비밀번호 입력
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# 로그인 버튼
login_btn = browser.find_element(By.CSS_SELECTOR,"#btn_login")
login_btn.click()
time.sleep(5)

press = 0

while True:
    # 과목 검색 버튼
    search_btn = browser.find_element(By.CSS_SELECTOR, "#tabs1")
    search_btn.click()
    time.sleep(0.3)

    # 꾸러미 신청 목록 버튼
    basket_btn = browser.find_element(By.CSS_SELECTOR, "#tabs2")
    basket_btn.click()
    time.sleep(0.3)
    press += 1

    # 수강인원
    people = browser.find_element(By.CSS_SELECTOR, "#grid01 > tr:nth-child(2) > td:nth-child(12)").text
    
    if people != '120':
        apply_btn = browser.find_element(By.CSS_SELECTOR, "#grid01 > tr:nth-child(2) > td:nth-child(2) > a") # 신청버튼
        apply_btn.click()
        time.sleep(1)
        # 경고 대화상자 다루기
        try:
            alert = Alert(browser)
            alert_text = alert.text
            if "신청 하시겠습니까?" in alert_text:
                alert.accept()  # "확인" 버튼 클릭
                time.sleep(1)
                try:
                    alert2 = Alert(browser)
                    alert2_text = alert2.text
                    if "수강인원 초과입니다." in alert2_text:
                        alert2.accept()
                    if "신청" in alert2_text:
                        alert2.accept()
                except Exception as e:
                    print("경고 대화상자 다루기 실패! :", e)
        except Exception as e:
            print("경고 대화상자 다루기 실패:", e)

    if press >= 1000:
        browser.refresh()
        time.sleep(2)
        press = 0