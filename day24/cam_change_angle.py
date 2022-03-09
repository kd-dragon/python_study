import cv2

prev = {"event" : 13} # 엔터키의 Ascii code 13

def change_angle(img, x, prev):
    ### 가만히 있어도 계속 x는 -1 로 들어온다!

    # 키보드 왼쪽키
    if x == 0x250000:
        frame = cv2.flip(img, 1)  # 이미지 좌우 반전(1), 이미지 상하 반전(0)
        prev['event'] = 0x250000
    # 키보드 오른쪽키
    elif x == 0x260000:
        frame = cv2.flip(img, 0)  # 이미지 좌우 반전(1), 이미지 상하 반전(0)
        prev['event'] = 0x260000
    # 키보드 아래키
    elif x == 0x270000:
        frame = cv2.flip(img, -1) # 이미지 좌우 반전(1), 이미지 상하 반전(0)
        prev['event'] = 0x270000
    # 키보드 윗쪽키
    elif x == 0x280000:
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        prev['event'] = 0x280000
    elif x == 13:
        prev['event'] = 13
        return img
    else:
        frame = change_angle(img, prev['event'], prev)
        # prev['event'] => 딕셔너리 이름이 prev 그 안의 'event' 라는 key 의 value 가 남는다.
        # 재귀 호출 (자기 자신을 호출하는 방식)
    return frame


cap = cv2.VideoCapture("funny.mp4")

if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000 / fps)
    # print(f"FPS: {fps}, Delay: {delay}")

    while True:
        ret, img = cap.read()
        # Boolean, Numpy 배열 객체를 쌍으로 갖는 튜플 객체를 반환 (ret이 False 면 프레임 읽기 실패 , 파일의 끝에 도달했거나 장치에 문제가 있을경우)
        if ret:  # 프레임이 정상이라면
            x = cv2.waitKeyEx(delay)  # 25ms 지연
            frame = change_angle(img, x, prev)

        cv2.imshow('camera', frame)  # 화면에 표시

        if x == 27:
            break

cap.release()
cv2.destroyAllWindows()