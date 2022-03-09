import cv2

img_background = cv2.imread("./image/1.jpg", cv2.IMREAD_COLOR) #flag =>이미지를 칼라로 불러올것이냐???? , GRAYSCALE

print(img_background)
img_background = img_background - img_background
print(img_background)
print("################################################")
print(type(img_background))
print(img_background.dtype)
cv2.imshow("IMAGE BASIC", img_background)

x = cv2.waitKey()
print(x)

cv2.imwrite("result.png", img_background)

img_gray = cv2.cvtColor(img_background, cv2.COLOR_BGR2GRAY)

#cv2.destroyAllWindows()

cv2.imshow("IMAGE GRAY", img_gray)
y = cv2.waitKey()

cv2.imwrite("result2.png", img_gray)
