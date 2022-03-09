import cv2
import time


# 마우스 이벤트 ㅎ마수를 미리 선언한다!
def processMouseEvent(event, x, y, flags, param):
    global size

    print(event, x, y, flags)
    if cv2.EVENT_LBUTTONDOWN & flags:
        cv2.circle(img, (x, y), size, colors['black'], -1)
        cv2.imshow(title, img)
    elif flags == 2:
        cv2.circle(img, (x, y), size, colors['red'], -1)
        cv2.imshow(title, img)
    elif flags == 4:
        cv2.circle(img, (x, y), size, colors['white'], -1)
        cv2.imshow(title, img)
    elif event == cv2.EVENT_MOUSEWHEEL:
        cv2.circle(img, (x, y), size, colors['green'], -1)
        cv2.imshow(title, img)


colors = {'black': (0, 0, 0),
          'red': (0, 0, 255),
          'white': (255, 255, 255),
          'green': (0, 255, 0)
          }

title = "mouse"
img = cv2.imread('blank_img.jpg')
cv2.imshow(title, img)

size = 10

cv2.setMouseCallback("mouse", processMouseEvent)  # 1. window name(title) , 콜백함수이름(processMouseEvent) , param (특정 파라미터)

# key = cv2.waitKey(0)
while True:
    key = cv2.waitKey(0)  # 대기 (블로킹)
    print(key)
    if key == 27:
        break
    elif key == ord('['):
        size -= 5
        print('size :', size)
    elif key == ord(']'):
        size += 5
        print('size :', size)
    else:
        continue

