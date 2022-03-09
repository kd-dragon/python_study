import cv2

video_file = "funny.mp4"

cap = cv2.VideoCapture(video_file)

if cap.isOpened():
    ret = True
    while ret:
        ret, img = cap.read()
        # Boolean , Numpy 배열 객체 ->>> 쌍으로 갖는 튜플 객체를 리턴!
        # Boolean(ret) -> False ( 파일의 끝에 도달했을때, 장치에 문제가있다, 파일이 깨졌다)
        if ret:
            cv2.imshow("VIDEO IMAGE !!!!", img)
            key = cv2.waitKey(25) #시간 단위: ms 밀리초 (1초: 1000ms)
            if key == 27 :
                break
else:
    print("can't open video.")

cv2.destroyAllWindows()
cap.release()






