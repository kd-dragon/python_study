import cv2

video_file = "funny.mp4"

cap = cv2.VideoCapture(video_file)

# CAP_PROP_FRAME_WIDTH: 프레임 폭
# CAP_PROP_FRAME_HEIGHT: 프레임 높이
# CAP_PROP_FPS: 초당 프레임의 수
# CAP_PROP_ZOOM: 카메라 줌

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FPS))
print(cap.get(cv2.CAP_PROP_ZOOM))

if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000/fps) ## 1s == 1000ms
    print(f"FPS: {fps}, Delay: {delay}")
    while True:
        ret, img = cap.read()
        # Boolean, Numpy 배열 객체를 쌍으로 갖는 튜플 객체를 반환 (ret이 False 면 프레임 읽기 실패 , 파일의 끝에 도달했거나 장치에 문제가 있을경우)

        if ret:  # 프레임이 정상이라면
            cv2.imshow(video_file, img)   # 화면에 표시
            x = cv2.waitKey(delay)    # 25ms 지연
            if x != -1:
                break
        else:
            break
else:
    print("can't open video.")
cap.release()
cv2.destroyAllWindows()