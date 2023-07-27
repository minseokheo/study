# requests 불러오기
import requests

# headers에 'User-Agent' 값 넣기
headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

# url에 주소 넣기
url = "https://www.transfermarkt.com/"

# requests.get()으로 요청하기
r = requests.get(url, headers=headers)
# status_code 응답확인하기 => 200이 나와야함
print(r.status_code)

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters: and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and the lived at the bottom of a well.</p>

<p class="story>...</p>"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# p 태그 정보 가져오기 (처음 나오는 것 한 개)
print(soup.p) # = print(soup.find('p'))

# a 태그에 있는 'href' 속성값 가져오기 (처음 나오는 것 한 개)
print(soup.find('a')['href']) # = print(soup.a['href'])

# a 태그에 있는 텍스트 가져오기 (처음 나오는 것 한 개)
print(soup.find('a').text) # = print(soup.find('a').get_text())

# a 태그에 있는 요소들 모두 가져오기
print(soup.find_all('a'))

# 두번째 a태그에 있는 정보 가져오기
print(soup.find_all('a')[1])

# a 태그에 있는 'href' 속성값 모두 가져오기
a_list = soup.find_all('a')
for i in a_list:
    print(i['href'])

# a 태그에 있는 텍스트 모두 가져오기
a_list = soup.find_all('a')
for i in a_list:
    print(i.text)

# 태그와 속성값을 같이 넣어 찾아오기
# a 태그이면서 class가 sister인 값 모두 찾아오기
print(soup.find_all("a", class_="sister"))
print(soup.find_all("a", {"class":"sister"}))

# a 태그이면서 id가 link3인 요소들 모두 찾기
print(soup.find_all("a", id="link3"))
print(soup.find_all("a", {"id":"link3"}))