import cv2

img = cv2.imread("3.jpg")

title = "Movement"
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
x, y = 100, 100
cv2.imshow(title, img)
while True:

    cv2.moveWindow(title, x, y)

    key = cv2.waitKey(0)

    if key == ord('g'):  # 좌측 방향키
        x -= 10
    elif key == ord('h'):  #아래 방향키
        y += 10
    elif key == ord('j'):  #우측 방향키
        x += 10
    elif key == ord('y'):  #윗쪽 방향키
        y -= 10
    elif key == ord('q') or key == 27:
        break
