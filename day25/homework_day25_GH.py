import cv2
import time

video_file = "funny.mp4"

cap = cv2.VideoCapture(video_file)

print("가로:", cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 프레임 폭
print("높이:", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 프레임 높이
print("프레임:", cap.get(cv2.CAP_PROP_FPS))  # 초당 프레임 수
print("카메라 줌:", cap.get(cv2.CAP_PROP_ZOOM))  # 카메라 줌

if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000 / fps)
    print(f"FPS: {fps}, Delay: {delay}")  # 파이썬 f-스트링 / 3.6 버전부터 지원.

    isProblem = True

    while isProblem:

        ret, img = cap.read()
        # Boolean , Numpy 배열 객체 ->>>> 쌍으로 갖는 튜플 객체를 리턴!
        # Boolean(ret) -> False (파일의 끝에 도달했을 때, 장치에 문제가 있다, 파일이 깨졌다)
        isProblem = ret
        input_key = 0

        if ret:

            key = cv2.waitKeyEx(delay)

            if key == 0x1B:  # ESC 16진수 :27
                break

            elif key == 0x250000:  # 0x250000 == left
                input_key = 1

                img = cv2.flip(img, 1)

                cv2.imwrite("xFlip.png", img)
                print("left_key")



            elif key == 0x270000:  # 0x270000 == right
                input_key = 1

                img = cv2.flip(img, 0)

                cv2.imwrite("yFlip.png", img)
                print("right_key")


            elif key == 0x260000:  # 0x270000 == up
                input_key = 1

                img = cv2.flip(img, -1)

                cv2.imwrite("xyFlip.png", img)
                print("up_key")

            elif key == 0x280000:  # 0x270000 == down
                input_key = 1

                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                cv2.imwrite("greyColor.png", img)
                print("down_key")

        else:
            print("can't open video.")

        if input_key == 0:

            cv2.imshow("VIDEO IMAGE !!!! /  ESC - 'Close' ", img)

        elif input_key == 1:
            time.sleep(1.1)
            cv2.imshow("VIDEO IMAGE !!!! /  ESC - 'Close' ", img)

cap.release()  # 메모리를 반환
cv2.destroyAllWindow()

