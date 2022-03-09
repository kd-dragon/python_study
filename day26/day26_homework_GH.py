import cv2

img = cv2.imread('blank_img.jpg')


# 실습
cv2.line(img, (50, 150), (100, 100), (0,0,255))
cv2.line(img, (200, 150), (250, 100), (0,0,255))

cv2.line(img, (100, 100), (250, 100), (0,255,0))
cv2.line(img, (50, 150), (200, 150), (0,255,0))

cv2.line(img, (50, 150), (50, 300), (0,0,0))
cv2.line(img, (200, 150), (200, 300), (0,0,0))
cv2.line(img, (250, 100), (250, 250), (0,0,0))

cv2.line(img, (50, 300), (200, 300), (255,0,0))
cv2.line(img, (200, 300), (250, 250), (255,0,0))


cv2.imshow('lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()