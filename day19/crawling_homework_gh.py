import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
print(url)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

table = soup.select('tr')

ranking_list = []
searchList = []

for i in table:

    append_list = []

    # 타이틀 긁어오는 부분

    try:

        title_txt = i.find('a').text #None

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

    ranking_list.append(append_list)

print(ranking_list)

keyword = input('검색어를 입력하시오. : ')

for i in range(0, 1):

    count = 0

    for i in ranking_list:

        if keyword in i[0]:

            print("-----------------------")
            print("#영화명 :", i[0])
            print("#순위 :", i[1])
            searchList.append(i)

            count += 1
        else:
            continue

    if count == 0:
        print("-----------------------")
        print("목록에 없는 영화입니다.")

f = open('movie_ranking.csv', 'w', newline='')
writer = csv.writer(f)

for i in searchList:
    writer.writerow(i)

f.close()
print('########## csv 쓰기완료 되었습니다. ##########')






