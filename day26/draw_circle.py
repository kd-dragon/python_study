import cv2

img = cv2.imread('blank_img.jpg')

# 원 그리기 (난이도 하)
# cv2.circle( img, center, radius, color, thickness, lineType )
# => [ 파라미터 종류 ]
# 1. img: 그림 이미지
# 2. center: 원점 좌표 (x,y) -> 원의 중심 좌표
# 3. radius : 원의 반지름 길이
# 4. color : 선 색상, (Blue, Green, Red), 0 ~ 255
# (생략가능) 5. thickness=1:  선 두께 (-1: 색으로 꽉 채우기)
# (생략가능) 6. lineType: 선 그리기 형식 (cv2.LINE_4: 4연결 선 알고리즘, cv2.LINE_AA: 안티에일리어싱-> 계단현상없음)


# 원점(150,150), 반지름 100
cv2.circle(img, (150, 150), 100, (255,0,0))
# 원점(300,150), 반지름 70
cv2.circle(img, (300, 150), 70, (0,255,0), 5)
# 원점(400,150), 반지름 50,
cv2.circle(img, (400, 150), 50, (0,0,255), -1)

cv2.imshow('circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()