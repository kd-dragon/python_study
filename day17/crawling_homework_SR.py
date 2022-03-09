from bs4 import BeautifulSoup
import requests

def cartoon_list(url):
    res = requests.get(url)
    print("응답코드 : ", res.status_code)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')
    titles = soup.find('div', attrs={'class':'detail'})
    print((titles.find('h2').text.replace('\n', '').replace('\r', '').replace('\t',' ').replace(' ','')))
    cartoons = soup.find_all("td", attrs={"class": "title"})

    for link1 in cartoons:
        a = link1.find('a').text
        b = link1.find('a')['href']
        print('제목:',a,'https://comic.naver.com'+ b)

cartoon_list("https://comic.naver.com/webtoon/list.nhn?titleId=641253&weekday=fri")