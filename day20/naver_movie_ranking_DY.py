import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
html = urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

category = soup.select('option')

div_tap = []
for i in soup.select('div.tab_type_6 > ul > li > a'):
    div_tap.append(i.attrs['href'])

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
print("#################################")
for i in table:

    append_list = []
    title_txt = i.select("td.title > div.tit5 > a")

    for x in title_txt:
        append_list.append(x.attrs['title'])
        append_list.append(x.attrs['href'])

    try:
        ranking_txt = i.select("td.ac > img")[0]['alt']
    except IndexError:
        continue

    append_list.append(ranking_txt)
    ranking_list.append(append_list)

###########################################################################################
print("################################2#")

for i in range(0, 1):

    for i in ranking_list:
        print("-----------------------")
        print("#영화명 :", i[0])
        print("#순위 :", i[2])
        print("#링크 :", 'https://movie.naver.com' + i[1])
