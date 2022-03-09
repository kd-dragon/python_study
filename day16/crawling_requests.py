from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import requests

url = "https://comic.naver.com/webtoon/weekday.nhn"

res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
print("응답코드 : ", res.status_code)

if res.status_code == requests.codes.ok:
    print("정상입니다.")
else:
    print("문제가 발생하였습니다. [오류코드 ", res.status_code, "]")


soup = BeautifulSoup(res.text, 'lxml')

# 특정 태그의 속성을 딕셔너리 형태로 출력
print(soup.a.attrs)
# 특정 태그의 특정 속성 값 가져오기
print(soup.a['href'])

# 특정 버튼을 찾기 (오른쪽 인기급상승 만화 목록 중 class 값이 rank01인 것 가져오기)
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1)

#네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class", "title"})
for cartoon in cartoons:
    print(cartoon.get_text())

