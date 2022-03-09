#BeautifulSoup4 -> Html 쉽게 다룰수있게하는 모듈
#urlopen -> url로 해당 위치에 접근 및 데이터 가져오기


import urllib.request
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='

keyword = input('검색어를 입력하세요')
finalUrl = url + urllib.parse.quote_plus(keyword)
#urllib.parse.quote_plus(검색어) : 한글 검색어를 인코딩해준다.
print(finalUrl)
massiveData = urllib.request.urlopen(finalUrl).read() #요청한 URL을 읽어온다
soup = BeautifulSoup(massiveData, 'html.parser') #위에서 읽어온 데이터를 Html 형식으로 파싱(포장)한다.
#a = soup.find(class_='lnk_tit') 검색한 결과중 1개만 가져온다
a = soup.find_all(class_='lnk_tit') # 검색한 결과 전체를 가져와 List로 반환한다.

print(a)
print(len(a))

for i in a:
    print(i)
