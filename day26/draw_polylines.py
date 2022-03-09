import cv2
import numpy as np

img = cv2.imread('blank_img.jpg')

# 다각형 그리기 (난이도 중)
# cv2.polylines ( img, points, isClosed, color, thickness, lineType )
# => [ 파라미터 종류 ]
# 1. img: 그림 이미지
# *2. points: 꼭지점 좌표 (Numpy 배열 리스트)
# *3. isClosed : 닫힌 도형 여부, True/False
# 4. color : 선 색상, (Blue, Green, Red), 0 ~ 255
# (생략가능) 5. thickness=1:  선 두께
# (생략가능) 6. lineType: 선 그리기 형식 (cv2.LINE_4: 4연결 선 알고리즘, cv2.LINE_AA: 안티에일리어싱-> 계단현상없음)


# Numpy array로 좌표 생성
# 번개 모양 선 좌표
pts1 = np.array([[50,50], [150,150], [100,140],[200,240]], dtype=np.int32)
# 삼각형 좌표
pts2 = np.array([[350,50], [250,200], [450,200]], dtype=np.int32)
# 삼각형 좌표
pts3 = np.array([[150,300], [50,450], [250,450]], dtype=np.int32)
# 5각형 좌표
pts4 = np.array([[350,250], [450,350], [400,450], [300,450], [250,350]], dtype=np.int32)

# 다각형 그리기
cv2.polylines(img, [pts1], False, (255,0,0))       # 번개 모양 선 그리기
cv2.polylines(img, [pts2], False, (0,0,0), 10)     # 3각형 열린 선 그리기
cv2.polylines(img, [pts3], True, (0,0,255), 10)    # 3각형 닫힌 도형 그리기
cv2.polylines(img, [pts4], True, (0,0,0))          # 5각형 닫힌 도형 그리기

cv2.imshow('polyline', img)
cv2.waitKey(0)
cv2.destroyAllWindows()