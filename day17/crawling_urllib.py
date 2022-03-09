from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import requests

url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="


keyword = input('검색어를 입력하세요')
finalUrl = url + quote_plus(keyword)
res = urlopen(finalUrl).read()


soup = BeautifulSoup(res, 'lxml')
#print(soup)

print(soup.find_all('a'))
list = soup.find_all('a')
# attrs 속성을 딕셔너리 형태로 출력
for img in list:
    print(img.attrs)
    print(img['href'])