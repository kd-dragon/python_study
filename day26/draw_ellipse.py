import cv2

img = cv2.imread('blank_img.jpg')

# 타원, 호 그리기 (난이도 상)
# cv2.ellipse( img, center, axes, angle, from, to, color, thickness, lineType )
# => [ 파라미터 종류 ]
# 1. img: 그림 이미지
# 2. center: 원점 좌표 (x,y) -> 원의 중심 좌표
# 3. axes : 기준 축 길이
# 4. angle : 기준 축 회전 각도
# 5. from : 호를 그릴 시작 각도
# 6. to : 호를 그릴 끝 각도
# 7. color : 선 색상, (Blue, Green, Red), 0 ~ 255
# (생략가능) 8. thickness=1:  선 두께 (-1: 색으로 꽉 채우기)
# (생략가능) 9. lineType: 선 그리기 형식 (cv2.LINE_4: 4연결 선 알고리즘, cv2.LINE_AA: 안티에일리어싱-> 계단현상없음)



# 원점(50,300), 반지름(50), 회전 0, 0도 부터 360도 그리기
cv2.ellipse(img, (50, 300), (50, 50), 0, 0, 360, (0,0,255))
# 원점(150, 300), 아래 반원 그리기
cv2.ellipse(img, (150, 300), (50, 50), 0, 0, 180, (255,0,0))
#원점(200, 300), 윗 반원 그리기
cv2.ellipse(img, (200, 300), (50, 50), 0, 181, 360, (0,0,255))

# 원점(325, 300), 반지름(75,50) 납작한 타원 그리기
cv2.ellipse(img, (325, 300), (75, 50), 0, 0, 360, (0,255,0))
# 원점(450,300), 반지름(50,75) 홀쭉한 타원 그리기
cv2.ellipse(img, (450, 300), (50, 75), 0, 0, 360, (255,0,255))

# 원점(50, 425), 반지름(50,75), 회전 15도
cv2.ellipse(img, (50, 425), (50, 75), 15, 0, 360, (0,0,0))
# 원점(200,425), 반지름(50,75), 회전 45도
cv2.ellipse(img, (200, 425), (50, 75), 45, 0, 360, (0,0,0))

# 원점(350,425), 홀쭉한 타원 45도 회전 후 아랫 반원 그리기
cv2.ellipse(img, (350, 425), (50, 75), 45, 0, 180, (0,0,255))
# 원점(400,425), 홀쭉한 타원 45도 회전 후 윗 반원 그리기
cv2.ellipse(img, (400, 425), (50, 75), 45, 181, 360, (255,0,0))

cv2.imshow('ellipse', img)
cv2.waitKey(0)
cv2.destroyAllWindows()