import cv2

# 마우스 이벤트 함수를 미리 선언한다!
def processMouseEvent(event, x, y, flags, param):
    print(event, x, y, flags)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 30, colors['black'], -1)
        cv2.imshow(title, img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 30, colors['red'], -1)
        cv2.imshow(title, img)
    elif event == cv2.EVENT_MBUTTONDOWN:
        cv2.circle(img, (x,y), 30, colors['blue'] ,-1)
        cv2.imshow(title, img)
    elif event == cv2.EVENT_MOUSEWHEEL:
        cv2.circle(img, (x, y), 30, colors['green'],-1)
        cv2.imshow(title, img)


colors = {'black':(0,0,0),
          'red':(0,0,255),
          'blue':(255,0,0),
          'green':(0,255,0)
          }


title = "mouse"
img = cv2.imread('blank_img.jpg')
cv2.imshow(title, img)


# 1. window_name(title), 콜백함수이름 ( processMouseEvent ) , param (특정 파라미터)
cv2.setMouseCallback("mouse", processMouseEvent)


while True:
    if cv2.waitKey(0) == 27:
        break

cv2.destroyAllWindows()


