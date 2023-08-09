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
pyperclip.copy("2018113085")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# 아이디 입력창
id = browser.find_element(By.CSS_SELECTOR, "#userId")
id.click()
pyperclip.copy("tig06015")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# 비밀번호 입력창
pw = browser.find_element(By.CSS_SELECTOR, "#pssrd")
pw.click()
pyperclip.copy("Love998100!")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# 로그인 버튼
login_btn = browser.find_element(By.CSS_SELECTOR,"#btn_login")
login_btn.click()
time.sleep(5)

while True:
    press = 0

    # 과목 검색 버튼
    search_btn = browser.find_element(By.CSS_SELECTOR, "#tabs1")
    search_btn.click()
    time.sleep(0.1)

    # 꾸러미 신청 목록 버튼
    basket_btn = browser.find_element(By.CSS_SELECTOR, "#tabs2")
    basket_btn.click()
    time.sleep(0.1)
    press += 1

    # 수강인원
    people = browser.find_element(By.CSS_SELECTOR, "#grid01 > tr:nth-child(2) > td:nth-child(12)").text
    
    if people != '120':
        apply_btn = browser.find_element(By.CSS_SELECTOR, "#grid01 > tr:nth-child(2) > td:nth-child(2) > a") # 신청버튼
        apply_btn.click()
        time.sleep(2)
        # 경고 대화상자 다루기
        try:
            alert = Alert(browser)
            alert_text = alert.text
            if "신청 하시겠습니까?" in alert_text:
                alert.accept()  # "확인" 버튼 클릭
        except Exception as e:
            print("경고 대화상자 다루기 실패:", e)
        time.sleep(1)

    if press >= 11000:
        browser.refresh()
        time.sleep(1)
    


"""
while people == '120': # 수강정원 120명
    if people != '120':
        apply = browser.find_element(By.CSS_SELECTOR, "#grid01 > tr:nth-child(2) > td:nth-child(2) > a") # 신청버튼
        apply.send_keys(Keys.RETURN)
    body = browser.find_element_by_tag_name('body')
    body.send_keys(Keys.F5)
    time.sleep(2)
"""
"""
initial_html = browser.page_source

while True:
    # 웹 페이지 열기
    browser.get(f'https://sugang.knu.ac.kr/web/stddm/lssrq/sugang/appcr.knu?login=true')
    current_html = browser.page_source
    
    # 이전과 현재 HTML을 비교하여 변화를 감지
    if current_html != initial_html:
        print("변화가 감지되었습니다! 알람을 보냅니다.")
        # 여기에서 알람을 보내는 작업을 추가할 수 있습니다.
        
        # 변화가 감지된 후에는 현재 HTML을 새로운 기준으로 설정
        initial_html = current_html
    
    # 일정 간격으로 웹 페이지를 확인 (예: 1분마다)
    time.sleep(60)

# 브라우저 종료
browser.quit()
"""