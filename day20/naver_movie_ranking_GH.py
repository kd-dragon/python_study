import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
html = urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

category = soup.select('option')

# 카테고리를 긁어옴###########################################################################################

category_list = []

for i in category:

    append_list = []

    try:

        category_num = i.attrs['value']
        append_list.append(category_num)

        category_name = i.text
        append_list.append(category_name)

        print(category_num, "==", category_name)

    except TypeError:

        continue

    category_list.append(append_list)

# 카테고리를 선택 & 출력###########################################################################################

keyword = input("영화장르의 '번호'를 타이핑 해주세요!")

for i in category_list:

    if keyword in i:
        print("==============================================")
        print("%%%% 카테고리 번호 : ", i[0])
        print("%%%% 영화 장르 : ", i[1])
        print("==============================================")

# URL 다시 선언 ###########################################################################################


url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20210226&tg=' + keyword
html = urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

table = soup.select('tr')

# 영화를 긁어옴###########################################################################################
ranking_list = []

for i in table:

    append_list = []

    # 타이틀 긁어오는 부분

    try:

        title_txt = i.find('a').text

        append_list.append(title_txt)

    except AttributeError:

        continue

    # 랭킹 긁어 오는 부분
    try:
        ranking_txt = i.find('img')['alt']

        if "up" in ranking_txt or "down" in ranking_txt or "na" in ranking_txt:
            continue

        append_list.append(ranking_txt)

    except TypeError:

        continue

    # 링크 긁어 오는 부분

    link_txt = i.find('a')['href']
    append_list.append(link_txt)

    # ranking_list 에 추가

    ranking_list.append(append_list)
###########################################################################################


for i in range(0, 1):

    for i in ranking_list:
        print("-----------------------")
        print("#영화명 :", i[0])
        print("#순위 :", i[1])
        print("#링크 :", 'https://movie.naver.com' + i[2])
