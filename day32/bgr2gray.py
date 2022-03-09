import cv2
import numpy as np

img = cv2.imread('logo.png')

img2 = img.astype(np.uint16)                # dtype 변경 (평균값 연산시 3채널을 더하면 255보다 큰 값이 나올 수 있으므로)
b,g,r = cv2.split(img2)                     # 채널 별로 분리 (split 함수사용)

#b,g,r = img2[:,:,0], img2[:,:,1], img2[:,:,2] # 직접 분리

gray1 = ((b + g + r)/3).astype(np.uint8)    # 평균 값 연산후 dtype 변경 -> 부정확하다!

gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # BGR을 그레이 스케일로 변경
cv2.imshow('original', img)
cv2.imshow('gray1', gray1)
cv2.imshow('gray2', gray2)

cv2.waitKey(0)
cv2.destroyAllWindows()