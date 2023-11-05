import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요")
response = requests.get(f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}")