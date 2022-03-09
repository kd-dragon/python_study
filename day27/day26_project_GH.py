import cv2
import numpy as np

def draw(x, y):
    cv2.line(img, (50 + x, 150 + y), (100 + x, 100 + y), (0, 0, 255))
    cv2.line(img, (200 + x, 150 + y), (250 + x, 100 + y), (0, 0, 255))

    cv2.line(img, (100 + x, 100 + y), (250 + x, 100 + y), (0, 255, 0))
    cv2.line(img, (50 + x, 150 + y), (200 + x, 150 + y), (0, 255, 0))

    cv2.line(img, (50 + x, 150 + y), (50 + x, 300 + y), (0, 0, 0))
    cv2.line(img, (200 + x, 150 + y), (200 + x, 300 + y), (0, 0, 0))
    cv2.line(img, (250 + x, 100 + y), (250 + x, 250 + y), (0, 0, 0))

    cv2.line(img, (50 + x, 300 + y), (200 + x, 300 + y), (255, 0, 0))
    cv2.line(img, (200 + x, 300 + y), (250 + x, 250 + y), (255, 0, 0))


x = 0
y = 0

while True:
    key = cv2.waitKeyEx(0)   # 블로킹 상태 (입력이 들어올때까지 대기)

    if key == 27:  # ESC 아스키코드 :27
        break
    elif key == 0x250000:  # 0x250000 == left
        x -= 50
    elif key == 0x270000:  # 0x270000 == right
        x += 50
    elif key == 0x260000:  # 0x270000 == up
        y -= 50
    elif key == 0x280000:  # 0x270000 == down
        y += 50

    img = cv2.imread('blank_img.jpg')
    draw(x, y)

    cv2.imshow('test', img)

cv2.destroyAllWindows()
