# 문제: 네이버 웹툰중 좋아하는 웹툰의 최근 10개 화에 대한 링크를 출력하시오.

from bs4 import BeautifulSoup
import requests

# URL 입력 (ex)웹툰 초인의 시대)
url = "https://comic.naver.com/webtoon/list.nhn?titleId=730694&weekday=sat"

# 해당 URL의 데이터를 가져오기 (정리되지 않은 데이터 상태)
res = requests.get(url)

# 응답코드 출력 (200이면 정상, 그 외는 모두 비정상)
print("응답코드 : ", res.status_code)

# 응답코드가 200이 아니면 오류를 발생시키는 코드
res.raise_for_status()

# 가져온 데이터를 HTML 형식으로 정리 변환 (BeautifulSoup 모듈 사용)
soup = BeautifulSoup(res.text, 'lxml')

# 위 링크의 HTML에서 <td> 태그이면서 속성 class 값이 title 인 정보를 가져온다. ex) <td class='title> 어찌고 저쩌고 </td>
cartoons = soup.find_all("td", attrs={"class": "title"})

# 가져온 데이터를 출력해보자
# print(cartoons)

# 반복문을 사용해서 제목과 링크만 정리하여 출력하는 부분을 코딩하시오.
for cartoon in cartoons:
    title = cartoon.get_text()
    link = "https://comic.naver.com" + cartoon.a.attrs['href']
    title = title.replace("\r", "").replace("\n", "")
    print(title, link)




