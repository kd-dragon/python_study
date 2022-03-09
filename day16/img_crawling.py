from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import requests


url = "https://www.google.com/search?q=%EB%94%B8%EA%B8%B0&tbm=isch&ved=2ahUKEwjT8srvgMbuAhUBUJQKHeWaCdYQ2-cCegQIABAA&oq=%EB%94%B8%EA%B8%B0&gs_lcp=CgNpbWcQAzIECCMQJzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIAFCeMlilOGCMOmgAcAB4AIABlQGIAa0DkgEDMC4zmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=RowWYNO3LoGg0QTltaawDQ&bih=937&biw=1252"

req = requests.get('https://www.google.com/search?q=%EB%94%B8%EA%B8%B0&tbm=isch&ved=2ahUKEwjT8srvgMbuAhUBUJQKHeWaCdYQ2-cCegQIABAA&oq=%EB%94%B8%EA%B8%B0&gs_lcp=CgNpbWcQAzIECCMQJzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIAFCeMlilOGCMOmgAcAB4AIABlQGIAa0DkgEDMC4zmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=RowWYNO3LoGg0QTltaawDQ&bih=937&biw=1252', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'})
req.raise_for_status()

#keyword = input('검색어를 입력하세요')
#finalUrl = url + quote_plus(keyword)
#print(finalUrl)

soup = BeautifulSoup(req.text, 'lxml')

img = soup.find_all("img")
print(img)

n = 1
for i in img:
    imgUrl = i['src']
    print(imgUrl)
    with urlopen(imgUrl) as f:
        with open(str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n+=1
