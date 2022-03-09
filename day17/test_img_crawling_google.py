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

imgs = soup.find_all('img', attrs={'class':'rg_i Q4LuWd'})
imgUrls = []

for img in imgs:
    try:
        imgUrls.append(img.attrs['src'])
    except KeyError:
        imgUrls.append(img.attrs['data-src'])

n = 1


for i in imgUrls:
    print(i)
    urlretrieve(i, "./img/ " + search + str(n) + ".jpg")
    n += 1


for img_url in imgUrls:
    f = urlopen(img_url).read()
    file_data = open("./img/ " + search + str(n) + '.jpg', 'wb')
    file_data.write(f)
    file_data.close()
    n += 1


#for i in imgUrl:
#    print(i)
#    with urlopen(i) as f:
#        with open('./img/' + search + str(n) + '.jpg', 'wb') as h:
#            img_read = f.read()
#            h.write(img_read)
#        n += 1

driver.close()




