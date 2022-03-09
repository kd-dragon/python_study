#pip install BeautifulSoup4
#pip install urlopen
import urllib.request
from bs4 import BeautifulSoup


url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#print(soup)
title = soup.find_all(class_='bx _svp_item')
#find는 1개만 가져오기
#find_all은 조건에 맞는거 전체 가져오기
print(title)
print(len(title))

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])