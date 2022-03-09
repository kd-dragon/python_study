import cv2
import numpy as np

blue, red = (255,0,0),(0,0,255)         # 색상 값


class FocusHelper:
    def __init__(self, img):
        self.isDragging = False
        self.x0 = -1
        self.y0 = -1
        self.w = -1
        self.h = -1
        self.img = img


def onMouse(event, x, y, flags, param):     # 1. 마우스 이벤트 핸들 함수
    # print(f'event:{event}| x:{x} | y:{y} | flags:{flags} | param : {param}')
    if event == cv2.EVENT_LBUTTONDOWN:  # 2. 왼쪽 마우스 버튼 다운, 드래그 시작
        param.isDragging = True
        param.x0 = x
        param.y0 = y
    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스를 움직일 때
        if param.isDragging:                  # 드래그 진행 중
            img_draw = img.copy()       # 사각형 그림 표현을 위한 이미지 복제
            cv2.rectangle(img_draw, (param.x0, param.y0), (x, y), blue, 2) # 드래그 진행 영역 표시
            cv2.imshow('img', img_draw) # 사각형 표시된 그림 화면 출력
    elif event == cv2.EVENT_LBUTTONUP:  # 왼쪽 마우스 버튼을 떼었을 때
        if param.isDragging:                  # 드래그 중지
            param.isDragging = False
            param.w = x - param.x0                  # 드래그 영역 폭 계산
            param.h = y - param.y0                  # 드래그 영역 높이 계산
            print("x:%d, y:%d, w:%d, h:%d" % (param.x0, param.y0, param.w, param.h))
            if param.w > 0 and param.h > 0:         # 폭과 높이가 음수이면 드래그 방향이 옳음
                img_draw = img.copy()   # 선택 영역에 사각형 그림을 표시할 이미지 복제
                # 선택 영역에 빨간 사각형 표시
                # ROI : Region Of Interest (관심영역)
                cv2.rectangle(img_draw, (param.x0, param.y0), (x, y), red, 2)
                cv2.imshow('img', img_draw) # 빨간 사각형 그려진 이미지 화면 출력
                roi = img[param.y0:(param.y0 + param.h), param.x0:(param.x0 + param.w)] # 원본 이미지에서 선택 영영만 ROI로 지정
                cv2.imshow('cropped', roi)  # ROI 지정 영역을 새창으로 표시
                cv2.moveWindow('cropped', x, y) # 새창을 화면 좌측 상단에 이동
                cv2.imwrite('./cropped.jpg', roi)   # ROI 영역만 파일로 저장
                print("croped success")
            else:
                cv2.imshow('img', img)  # 드래그 방향이 잘못된 경우 사각형 그림ㅇㅣ 없는 원본 이미지 출력
                print("좌측 상단에서 우측 하단으로 영역을 드래그 하세요.")

img = cv2.imread('test.jpg')

helper = FocusHelper(img)

cv2.imshow('img', img)
# 마우스 이벤트 등록
cv2.setMouseCallback('img', onMouse, helper)
cv2.waitKey()
cv2.destroyAllWindows()