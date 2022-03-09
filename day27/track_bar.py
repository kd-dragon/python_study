import cv2

# 트랙바: 슬라이드 모양의 인터페이스, 마우스로 버튼을 움직여서 값을 입력받는 GUI 요소

# cv2.getTrackbar(trackbar_name, win_name, value, count, onChange): 트랙바 생성 함수
 # trackbar_name = 트랙바 이름
 # win_name = 윈도우 창 이름 (트랙바를 표시할 창 이름, ex) title)
 # value = 트랙바 초기값, 0~count 사이의 값
 # count = 트랙바 눈금 개수, 트랙바가 표시할 수 있는 최대값
 # onChange = TrackbarCallback (트랙바 이벤트 핸들러 함수)

# TrackbarCallback(value) : 트랙바 이벤트 콜백함수
 # value: 트랙바가 움직인 새 위치 값 (= 마우스 이벤트와 동일)

# cv2.getTrackbarPos(trackbar_name, win_name): 트랙바의 값을 얻기 위한 함수
 # trackbar_name: 찾고자 하는 트랙바 이름
 # win_name : 트랙바가 있는 창의 이름
 # pos =  cv2.getTrackbarPos(trackbar_name, win_name)
 # pos : 트랙바의 위치값

win_name = 'Trackbar'

img = cv2.imread('blank_img.jpg')
cv2.imshow(win_name, img)


# 트랙바 이벤트 처리 함수
def trackbar_handler(value):
    # 'RGB' 각 트랙바 위치값 설정
    r = cv2.getTrackbarPos('R', win_name)
    g = cv2.getTrackbarPos('G', win_name)
    b = cv2.getTrackbarPos('B', win_name)
    switch = cv2.getTrackbarPos('Switch', win_name)
    # 0 : 비사용
    # 1 : 사용

    print(r, g, b, switch)

    # RGB -> BGR

    if switch == 0:
        img[:] = 255
        cv2.setTrackbarPos('R', win_name, 0)
        cv2.setTrackbarPos('G', win_name, 0)
        cv2.setTrackbarPos('B', win_name, 0)
    else:
        img[:] = [b, g, r]

    cv2.imshow(win_name, img)


cv2.createTrackbar('R', win_name, 0, 255, trackbar_handler)
cv2.createTrackbar('G', win_name, 0, 255, trackbar_handler)
cv2.createTrackbar('B', win_name, 0, 255, trackbar_handler)

## 사용 여부 트랙바 ##
cv2.createTrackbar('Switch', win_name, 0, 1, trackbar_handler)




while True:
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
