from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import re
import glob
from datetime import datetime
import os

# Chrome 옵션 설정
options = Options()
options.add_experimental_option("detach", True)

# 웹드라이버 실행
driver = webdriver.Chrome(options=options)

# 대상 블로그 포스트 URL
url = 'https://blog.naver.com/xuenxu/223864678788'
driver.get(url)
driver.maximize_window()
time.sleep(2)

# mainFrame으로 전환 (최초 댓글 버튼 찾기 전에)
try:
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "mainFrame"))
    )
    print("mainFrame으로 전환 성공")
except:
    print("mainFrame으로 전환 실패")
    driver.quit()
    exit()

# 최초 댓글 버튼 클릭 (mainFrame 안에서 찾기)
try:
    initial_comment_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#Comi223864678788"))
    )
    initial_comment_button.click()
    print("최초 댓글 버튼 클릭 성공")
    time.sleep(1) # 버튼 클릭 후 잠시 대기

    # 댓글 영역 로딩 완료까지 명시적으로 대기 (예시: 댓글 목록의 첫 번째 요소가 나타날 때까지)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li.u_cbox_comment"))
    )
    print("댓글 영역 로딩 완료 대기 성공")
    time.sleep(2) # 댓글 로딩 후 추가 대기

except:
    print("최초 댓글 버튼을 찾거나 클릭할 수 없거나, 댓글 영역 로딩에 실패했습니다.")
    driver.quit()
    exit()

current_folder_path = os.path.abspath('.')
print(f"현재 폴더의 절대 경로는: {current_folder_path}")

current_datetime_str = datetime.now().strftime('%Y.%m.%d_%H%M')
filename = os.path.join(current_folder_path, f"kbanknow_links_{current_datetime_str}.txt") # 현재 실행 날짜로 저장될 파일 이름

text_files = glob.glob(os.path.join(current_folder_path, "kbanknow_links_*.txt"))
base_datetime = None
first_run = not text_files

if first_run:
    print("첫 번째 실행: 모든 댓글 페이지에서 링크를 추출합니다 (역순).")
else:
    # .txt 파일이 있으면 가장 최근 파일 이름 추출 (생성 시간 기준)
    latest_file = max(text_files, key=os.path.getctime)
    print(f"발견된 가장 최근 text 파일: {latest_file}")
    try:
        file_datetime_str = os.path.splitext(os.path.basename(latest_file))[0].replace('kbanknow_links_', '').replace('_', '.')
        base_datetime = datetime.strptime(file_datetime_str, '%Y.%m.%d.%H%M')
        print(f"이전 기준 시간: {base_datetime}")
    except ValueError:
        print("오류: text 파일 이름이 'kbanknow_links_YYYY.MM.DD_HHMM.txt' 형식이 아닙니다. 모든 댓글을 추출합니다.")
        first_run = True
    except Exception as e:
        print(f"파일 처리 오류: {e}. 모든 댓글을 추출합니다.")
        first_run = True

all_kbanknow_links = set() # 중복 링크 제거를 위한 set

try:
    # 마지막 페이지 번호 추출
    last_page_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".commentbox_pagination span._lastPageNo"))
    )
    last_page = int(last_page_element.text)
    print(f"총 댓글 페이지 수: {last_page}")
    current_page = last_page
except:
    print("총 댓글 페이지 수를 추출할 수 없습니다. 1페이지로 간주하고 진행합니다.")
    current_page = 1
    last_page = 1

while current_page >= 1:
    print(f"현재 댓글 페이지 (링크 추출): {current_page}")

    # 현재 페이지 내 모든 댓글의 시간 정보 가져오기 (더 긴 대기)
    comment_time_elements = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.u_cbox_date'))
    )
    comment_times = [element.text for element in comment_time_elements]
    print(f"현재 페이지 (데이터 추출): {current_page}, 기준 시간: {base_datetime}")
    print(f"댓글 시간: {comment_times}")

    # 현재 페이지의 모든 댓글 요소 가져오기 (더 긴 대기)
    comment_elements = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.u_cbox_comment'))
    )

    # 스크롤 (고정값 유지)
    driver.execute_script("window.scrollTo(0, 1500);")
    time.sleep(1) # 로딩 대기

    for i, comment_time in enumerate(comment_times):
        try:
            comment_datetime = datetime.strptime(comment_time, '%Y.%m.%d. %H:%M')
            print(f"댓글 시간 (변환): {comment_datetime}")
            # 기존에 다운받았던 시간이 댓글을 적은 시간보다 더 이후라면 중단
            if not first_run and base_datetime and base_datetime > comment_datetime:
                break # 댓글 시간 루프 탈출
            else:
                # 'kbanknow' 포함된 링크만 추출
                link_elements = comment_elements[i].find_elements(By.CSS_SELECTOR, 'a.u_cbox_contents_link')
                for link in link_elements:
                    href = link.get_attribute('href')
                    if href and 'kbanknow' in href:
                        all_kbanknow_links.add(href)
        except ValueError:
            print(f"오류: 댓글 시간 형식 '{comment_time}'이 맞지 않습니다.")
        except Exception as e:
            print(f"댓글 처리 중 오류 발생: {e}")

    if not first_run and any(base_datetime and base_datetime > datetime.strptime(ct, '%Y.%m.%d. %H:%M') for ct in comment_times):
        print("이전 시간 이후의 댓글을 모두 처리했습니다.")
        break # while True 루프 탈출

    if current_page > 1:
        # 이전 페이지 버튼 클릭 시도 (더 긴 대기 및 JavaScript 클릭 시도)
        try:
            prev_button_selector = '//*[@id="naverComment_201_223864678788_ct"]/div[1]/div/div[2]/a[1]'
            # 이전 페이지 버튼이 나타날 때까지 최대 30초 대기 (mainFrame 안에서 찾기)
            prev_button = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, prev_button_selector))
            )
            if prev_button.is_enabled():
                print("이전 페이지 버튼 발견 및 클릭 시도")
                # JavaScript를 사용하여 클릭 시도
                driver.execute_script("arguments[0].click();", prev_button)
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'span.u_cbox_date')) # 다음 페이지 댓글 로딩 대기
                )
                print("이전 페이지로 이동")
                current_page -= 1
                time.sleep(2) # 페이지 이동 후 충분히 대기
            else:
                print("이전 페이지 버튼이 비활성화되어 있습니다.")
                break
        except:
            print("이전 페이지 버튼을 찾을 수 없거나 클릭할 수 없습니다.")
            break # 이전 페이지가 없으면 while True 루프 탈출
    else:
        print("1페이지까지 모든 링크를 추출했습니다.")
        break

# 모든 링크 수집 완료 후 파일에 저장
if all_kbanknow_links:
    with open(filename, 'w', encoding='utf-8') as f: # 현재 실행 날짜로 파일 생성
        for link in sorted(list(all_kbanknow_links)): # 중복 제거 후 정렬하여 저장
            f.write(f"{link}\n")
    print(f"총 {len(all_kbanknow_links)}개의 'kbanknow' 링크를 '{filename}' 파일에 저장했습니다.")
else:
    print("'kbanknow' 링크를 찾지 못했습니다.")

exit()