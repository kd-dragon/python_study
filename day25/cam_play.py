import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000/fps)
    # print(f"FPS: {fps}, Delay: {delay}")
    vcnt = 0
    hcnt = 0
    vhcnt = 0
    gcnt = 0

    while True:
        ret, img = cap.read()
        # Boolean, Numpy 배열 객체를 쌍으로 갖는 튜플 객체를 반환 (ret이 False 면 프레임 읽기 실패 , 파일의 끝에 도달했거나 장치에 문제가 있을경우)
        if ret:  # 프레임이 정상이라면
            frame = img
            x = cv2.waitKeyEx(delay)    # 25ms 지연
            print(x)
            # 마우스 왼쪽키
            if x == 0x250000:
                frame = cv2.flip(img, 1)  # 이미지 좌우 반전(1), 이미지 상하 반전(0)
                cv2.imwrite(f"vertical_{vcnt}.png", frame)
                vcnt += 1
            # 마우스 오른쪽키
            elif x == 0x270000:
                frame = cv2.flip(img, 0)  # 이미지 좌우 반전(1), 이미지 상하 반전(0)
                cv2.imwrite(f"horizon_{hcnt}.png", frame)
                hcnt += 1
            # 마우스 아래키
            elif x == 0x280000:
                frame = cv2.flip(img, -1)
                cv2.imwrite(f"vertical_horizon_{vhcnt}.png", frame)
                vhcnt += 1
            # 마우스 윗쪽키
            elif x == 0x260000:
                frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(f"gray_{gcnt}.png", frame)
                gcnt += 1

            cv2.imshow('camera', frame)  # 화면에 표시

            if x == 27:
                break
        else:
            break

cap.release()
cv2.destroyAllWindows()