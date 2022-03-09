import numpy as np
import cv2
img = cv2.imread('test.jpg')
x=200
y=80
w=80
h=80

box = img[y:y+h, x:x+w]
# 개발자들은 그림같은 거 코드로 표현할 때 폭(width), 높이(height)순으로 코딩하는데..일반적으로
# Numpy 배열은 행, 열 순으로 접근하기 때문에 반드시 높이, 폭 순으로 지정을 해야한다!!
print(box.shape)

# 이미지 복제하기
img[y:y+h, (x+w):(x+w)+w] = box
#cv2.rectangle(img, (x+w-1,y), ((x+w)+w, y+h), (0,255,0))

#cv2.rectangle(box, (0,0), (h-1, w-1), (0,255,0))
cv2.imshow("img", img)

#img2 = box.copy()
#cv2.imshow("box", img2)

key = cv2.waitKey(0)
cv2.destroyAllWindows()