from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import quote_plus
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests


search = input('검색어를 입력하세요')

keyword = quote_plus(search)
frontUrl = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
url = frontUrl + keyword
driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)

html = driver.page_source
#print(html)

soup = BeautifulSoup(html, 'lxml')
#print(soup)
#driver.close()


imgs = soup.select('._image._listImage')
#print(imgs)


imgUrl = []
for x in imgs:
    img = x.attrs['src']
    if 'https://search' in img:
        imgUrl.append(img)


n = 1
for i in imgUrl:
    print(i)
    urlretrieve(i, './img/' + search + str(n) + ".jpg")
    n += 1

driver.close()

