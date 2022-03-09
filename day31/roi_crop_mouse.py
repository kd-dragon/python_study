import cv2
import numpy as np

# 객체 지향적인 코딩 방식의 습관을 좀 기르자.
class focusHelper:
    # isDragging = False
    blue = (255, 0, 0)
    red = (0, 0, 255)

    def __init__(self, img):
        self.isDragging = False
        self.x0 = -1
        self.y0 = -1
        self.w = -1
        self.h = -1
        self.img = img


def onMouse(event, x, y, flags, param):  # 마우스 이벤트 핸들 함수  ---①
    print(param)
    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 마우스 버튼 다운, 드래그 시작 ---②
        isDragging = True
        x0 = x
        y0 = y
    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 움직임 ---③
        if isDragging:  # 드래그 진행 중
            img_draw = img.copy()  # 사각형 그림 표현을 위한 이미지 복제
            cv2.rectangle(img_draw, (x0, y0), (x, y), blue, 2)  # 드래그 진행 영역 표시
            cv2.imshow('img', img_draw)  # 사각형 표시된 그림 화면 출력
    elif event == cv2.EVENT_LBUTTONUP:  # 왼쪽 마우스 버튼 업 ---④
        if isDragging:  # 드래그 중지
            isDragging = False
            w = x - x0  # 드래그 영역 폭 계산
            h = y - y0  # 드래그 영역 높이 계산
            print("x:%d, y:%d, w:%d, h:%d" % (x0, y0, w, h))
            if w > 0 and h > 0:  # 폭과 높이가 음수이면 드래그 방향이 옳음 ---⑤
                img_draw = img.copy()  # 선택 영역에 사각형 그림을 표시할 이미지 복제
                # 선택 영역에 빨간 사각형 표시
                cv2.rectangle(img_draw, (x0, y0), (x, y), red, 2)
                cv2.imshow('img', img_draw)  # 빨간 사각형 그려진 이미지 화면 출력
                # ROI : Region Of Interest (관심 영역)
                roi = img[y0:y0 + h, x0:x0 + w]  # 원본 이미지에서 선택 영영만 ROI로 지정 ---⑥
                print(img)
                print("============================================")
                print(roi)
                # roi = img[x0:x0 + w, y0:y0 + h]  # 원본 이미지에서 선택 영영만 ROI로 지정 ---⑥
                cv2.imshow('cropped', roi)  # ROI 지정 영역을 새창으로 표시
                cv2.moveWindow('cropped', 0, 0)  # 새창을 화면 좌측 상단에 이동
                cv2.imwrite('./result/cropped.jpg', roi)  # ROI 영역만 파일로 저장 ---⑦
                print("croped.")
            else:
                cv2.imshow('img', img)  # 드래그 방향이 잘못된 경우 사각형 그림이 없는 원본 이미지 출력
                print("좌측 상단에서 우측 하단으로 영역을 드래그 하세요.")


img = cv2.imread('test.jpg')
helper = focusHelper(img)

# class 인스턴스화 시킬때 img를 넣어준다.
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse, helper)  # 마우스 이벤트 등록 ---⑧
cv2.waitKey()
cv2.destroyAllWindows()