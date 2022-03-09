from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import requests
import time

search = input('검색어를 입력하세요')

keyword = quote_plus(search)
frontUrl = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
url = frontUrl + keyword
print(url)

res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

#print(soup)
imgs = soup.find_all('img')
print(imgs)
imgUrl = []
for img in imgs:
    imgUrl.append(img.attrs['src'])

n = 1
for i in imgUrl:
    #print(i)
    f = urlopen(i).read()
    file_data = open(search + str(n) + '.jpg', 'wb')
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



#for i in imgUrl:
#    print(i)
#    urlretrieve(i, search + str(n) + ".jpg")
#    n += 1



