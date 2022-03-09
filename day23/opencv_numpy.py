import cv2
import numpy as np

img_background = cv2.imread("./image/1.jpg", cv2.IMREAD_COLOR)
print(type(img_background))
print(img_background)
print(img_background.dtype)
print(img_background.shape)
print(img_background.ndim)

img_gray = cv2.cvtColor(img_background, cv2.COLOR_BGR2GRAY)
print(type(img_gray))
print(img_gray)
print(img_gray.dtype)
print(img_gray.shape)
print(img_gray.ndim)

img_test = img_background - img_gray

cv2.imshow('img_test', img_test)
cv2.waitKey()