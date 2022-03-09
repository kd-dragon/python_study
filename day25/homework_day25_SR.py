import cv2
import time

video_file = 'funny.mp4'

cap = cv2.VideoCapture(video_file)

if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000/fps) ## 1s == 1000ms
    print(f"FPS: {fps}, Delay: {delay}")

    while True:
        ret, img = cap.read()

        if ret:
            cv2.imshow(video_file, img)
            key = cv2.waitKeyEx(delay)

            if key == 27:
                break
            elif key == 0x250000:
                i = cv2.flip(img,1)
                cv2.imwrite('flip1.png',i)
            elif key == 0x270000:
                i = cv2.flip(img,0)
                cv2.imwrite('flip2.png',i)
            elif key == 0x260000:
                i = cv2.flip(img,-1)
                cv2.imwrite('flip3.png',i)
            elif key == 0x280000:
                i = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                cv2.imwrite('flip4.png',i)

else:
    print("can't open video")

cv2.destroyAllWindows()
cap.release()