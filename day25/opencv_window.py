import cv2

img = cv2.imread("3.jpg")
img_gray = cv2.imread("3.jpg", cv2.IMREAD_GRAYSCALE)

window1 = "origin"
window2 = "gray"

cv2.namedWindow(window1, cv2.WINDOW_NORMAL)  # 임의의 크기(사용자가 지정한 크기), 창 크기 재조정 가능
cv2.namedWindow(window2, cv2.WINDOW_AUTOSIZE)  # 이미지와 같은 크기! 그러나! 창 크기 재조정이 불가능하다.

cv2.waitKey(0)

cv2.imshow(window1, img)
cv2.imshow(window2, img_gray)

cv2.waitKey(0)

cv2.moveWindow(window1, 0, 0)
cv2.moveWindow(window2, 100, 100)

cv2.waitKey(0)

cv2.resizeWindow(window1, 200, 700)
cv2.resizeWindow(window2, 200, 700)

cv2.waitKey(0)

cv2.destroyWindow(window2)

cv2.waitKey(0)
cv2.destroyAllWindows()