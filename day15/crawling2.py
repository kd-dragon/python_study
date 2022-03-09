import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


baseUrl = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EB%94%A9'
plusUrl = input('검색어를 입력하세요')

#urllib.parse.quote_plus(plusUrl)

url = baseUrl + plusUrl
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
title = soup.find_all(class_='sh_blog_title')

for i in title:
    print(i.attrs['title'])