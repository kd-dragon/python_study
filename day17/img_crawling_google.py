from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import quote_plus
from selenium import webdriver
from bs4 import BeautifulSoup


import requests
# https://chromedriver.chromium.org/downloads 크롬 드라이버 다운 받기

search = input('검색어를 입력하세요')

keyword = quote_plus(search)
print(keyword)
frontUrl = "https://www.google.com/search?q="
endUrl = "&hl=ko&sxsrf=ALeKk02e66ThAAnCqomzh1P6vCIEndnvPg:1612586102210&source=lnms&tbm=isch&sa=X&ved=2ahUKEwimv6qut9TuAhXKZt4KHYPWBF4Q_AUoAXoECAwQAw&biw=1920&bih=937"

url = frontUrl + keyword + endUrl
print(url)


driver = webdriver.Chrome()
driver.get(url)



html = driver.page_source

soup = BeautifulSoup(html, 'lxml')

# 특정 태그의 속성을 딕셔너리 형태로 출력
imgs = soup.find_all('img', attrs={'class':'rg_i Q4LuWd'})
imgUrl = []

for img in imgs:
    try:
        imgUrl.append(img.attrs['src'])
    except KeyError:
        imgUrl.append(img.attrs['data-src'])

n = 1
for i in imgUrl:
    print(i)
    urlretrieve(i, "./img/" + search + str(n) + ".jpg")
    n += 1

driver.close()



