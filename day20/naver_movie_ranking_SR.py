import csv
import requests
from bs4 import BeautifulSoup

# 딕셔너리사용 (키, value 세트)
genre_dic = {}
# genre_num = []
# genre_title = []

rank_movie_list = []
front_url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20210222'
res = requests.get(front_url)
soup = BeautifulSoup(res.text, 'lxml')


def genre():
    # genre_list_all = []
    for i in soup.find_all('option'):
        # genre_list = []
        try:
            value = i['value']
            text = i.text
            # 딕셔너리사용 (키, value 세트)
            genre_dic[value] = text

            # genre_list.append(value)
            # genre_list.append(text)
            # print(genre_list)
        except:
            continue

        # genre_list_all.append(genre_dic)

    # for i in genre_list_all:
    #    genre_num.append(i[0])
    #    genre_title.append(i[1])

# 장르 함수 호출 (딕셔너리에 영화 카테고리 종류 담는 함수)
genre()
print(genre_dic)

search = input('해당 장르의 숫자를 입력하세요. : ')
back_url = '&tg='

# tag_num = genre_num[int(search)]
tag_num = search  # 받은 번호 그대로 사용 (숫자말고 다른 입력은 예외처리는 생략)

print("선택된 장르 :: " + genre_dic.get(search))

res2 = requests.get(front_url+back_url+tag_num)
soup2 = BeautifulSoup(res2.text, 'lxml')


def ranking():

    # 랭크 태그 필터링
    movies_rank = soup2.select('tr')

    for i in movies_rank:

        append_list = []

        # 랭크 숫자 어펜드
        try:

            rank = i.find('img')['alt']

            if 'up' in rank or 'down' in rank or 'na' in rank:

                continue

            append_list.append(rank)

        except AttributeError:

            continue

        except TypeError:

            continue

        # 랭킹순으로 영화제목 어펜드
        try:

            title = i.find('a').text

            append_list.append(title)

            print(append_list)

        except AttributeError:

            continue

        rank_movie_list.append(append_list)

ranking()

with open('movie_ranking.csv', 'w', encoding='euc-kr', newline='') as f:

    write = csv.writer(f)
    write.writerows(rank_movie_list)


print('csv 쓰기완료')
