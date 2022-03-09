import os
import cv2
import matplotlib.pyplot as plt
import numpy as np



# plit.plot 대신 plt.imshow() 함수를 호출

img = cv2.imread('test.jpg')
img2 = cv2.imread('test.jpg')

#np = np.arange(10)
#print(np)
#print(np[::-1])


plt.imshow(img[:,:,(2,1,0)])
plt.xticks([])
plt.yticks([])
plt.show()

# plt.imshow() 함수는 컬러 채널 R, G, B 순으로 해석
# openCV 는 imread 할 때 B,G,R 순으로 만들어진다. 색상의 위치가 반대라서 색상이 이상해짐

