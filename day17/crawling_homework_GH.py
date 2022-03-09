from bs4 import BeautifulSoup
import requests

url = 'https://comic.naver.com/webtoon/list.nhn?titleId=670152&weekday=sun'

res = requests.get(url)

if res.status_code == requests.codes.ok:
    print("정상입니다.")
else:
    print("문제가 발생하였습니다. [오류코드 ", res.status_code, "]")

soup = BeautifulSoup(res.text, 'lxml')

cartoons = soup.find_all("td", attrs={"class": "title"})

titles = soup.find("div", attrs={"class": "detail"})

print(titles.find('h2').text)

for i in cartoons:
    title = i.find('a').text

    link = i.find('a')['href']
    naver = "https://comic.naver.com"

    naver_link = naver + link

    print(title, naver_link)

