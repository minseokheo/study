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

if not os.path.exists('inflearn/이것이 진짜 크롤링이다 - 실전편/구글_이미지_크롤링/고양이'):
    os.mkdir('inflearn/이것이 진짜 크롤링이다 - 실전편/구글_이미지_크롤링/고양이')

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

url = "https://www.google.com/search?q=%EA%B3%A0%EC%96%91%EC%9D%B4&sca_esv=591053097&tbm=isch&sxsrf=AM9HkKldQDN8ofjItoA4Rwg2P3tS4sxhdQ:1702621262071&source=lnms&sa=X&ved=2ahUKEwiN2oy85pCDAxW8QPUHHa38ATgQ_AUoAXoECAMQAw&biw=1920&bih=919&dpr=1"
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

# 썸네일 이미지 태그 추출
imgs = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

for i, img in enumerate(imgs, 1):
    # 이미지를 클릭해서 큰 사이즈를 찾아요
    # 클릭하다보면 element click intercepted 에러가 나요
    # javascript 로 클릭을 직접 하도록 만들어주면 됩니다.
    driver.execute_script("arguments[0].click();", img)
    time.sleep(1)

    # 큰 이미지 주소 추출
    try:
        target = driver.find_element(By.CSS_SELECTOR, ".sFlh5c.pT0Scc.iPVvYb")
        img_src = target.get_attribute('src')
    except:
        continue

    # 이미지 다운로드
    # 크롤링 하다보면 HTTP Error 403: Forbidden 에러가 납니다.
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozila/5.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(img_src, f"inflearn/이것이 진짜 크롤링이다 - 실전편/구글_이미지_크롤링/고양이/{i}.jpg")
