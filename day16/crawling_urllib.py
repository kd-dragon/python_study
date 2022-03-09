from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import requests

url = "https://www.google.com/search?q=%EB%94%B8%EA%B8%B0&sxsrf=ALeKk03OQcMZJ2AbuWM6Pcyttf7QjZ6b9w:1612095987372&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi-6K7FlcbuAhXUc3AKHTvGCRAQ_AUoAXoECBUQAw&biw=1778&bih=819"
res = urlopen(url).read()

#keyword = input('검색어를 입력하세요')
#finalUrl = url + quote_plus(keyword)

soup = BeautifulSoup(res, 'lxml')
#print(soup)

soup.find_all('a')

#atts 속성을 딕셔너리 형태로 출력
#print(soup.a.attrs)
#print(soup.a['href'])