import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

# api_txt_lines total_tit

# 태그 이름만 특정
# soup.select_one('p')
# soup.find('p')

# 태그 class 특정
# soup.select_one('.youngone')
# soup.find(attrs={'class':'youngone')

# 태그 이름과 class 모두 특정
# soup.select_one('p.youngone')
# soup.find('p', attrs={'class':'yongone'})

# 태그 id 특정
# soup.select_one('#junu')
# soup.find(attrs={'id':'junu')

# 태그 이름과 id 모두 특정
# soup.select_one('p#junu')
# soup.find('p', attrs={'id':'junu'})

# 태그 이름과 class, id 모두 특정
# soup.select_one('p.youngone#junu')
# soup.find('p', attrs={'id':'junu','class':'youngone'})

keyword = input('검색어를 입력하시오. : ')
search = quote_plus(keyword)
url = 'https://search.naver.com/search.naver?where=view&sm=tab_jum&query=' + search
print(url)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

total = soup.select('.api_txt_lines.total_tit')

print(total[0])


searchList = []

for i in total:
    temp = []
    temp.append(i.text) # 제목
    temp.append(i.attrs['href']) # 링크
    searchList.append(temp)


print(searchList[0])

f = open(keyword + '.csv', 'w', newline='')
writer = csv.writer(f)

for i in searchList:
    writer.writerow(i)
f.close()

print('########## 완료 되었습니다. ##########')