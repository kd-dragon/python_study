import cv2

img = cv2.imread('blank_img.jpg')

# 사각형 그리기 (난이도 하)
# cv2.rectangle( img, start, end, color, thickness, lineType )
# => [ 파라미터 종류 ]
# 1. img: 그림 이미지
# 2. start: 선 시작 지점 좌표 (x,y)
# 3. end : 선 끝 지점 좌표 (x,y)
# 4. color : 선 색상, (Blue, Green, Red), 0 ~ 255
# (생략가능) 5. thickness=1:  선 두께
# (생략가능) 6. lineType: 선 그리기 형식 (cv2.LINE_4: 4연결 선 알고리즘, cv2.LINE_AA: 안티에일리어싱-> 계단현상없음)

# 실습
# 좌상, 우하 좌표로 사각형 그리기
cv2.rectangle(img, (50, 50), (150, 150), (255,0,0) )
# 우하, 좌상 좌표로 사각형 그리기
cv2.rectangle(img, (300, 300), (100, 100), (0,255,0), 10 )
# 우상, 좌하 좌표로 사각형 채워 그리기 ---①
cv2.rectangle(img, (450, 200), (200, 450), (0,0,255), -1 )

cv2.imshow('rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()