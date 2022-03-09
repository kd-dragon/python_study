import cv2

img = cv2.imread('blank_img.jpg')

# 글씨 그리기 (난이도 중)
# cv2.putText( img, text, point, fontFace, fontSize, color, thickness, lineType)
# => [ 파라미터 종류 ]
# 1. img: 그림 이미지
# 2. text: 원표시할 문자열
# 3. point : 글씨를 표시할 좌표 (좌측 하단 기준) (x, y) 2차원 배열
# 4. fontFace : 글꼴
    # 4-1. cv2.FONT_HERSHY_PLAIN: 산세리프체 작은 글꼴
    # 4-2. cv2.FONT_HERSHEY_SIMPLEX: 산세리프체 일반 글꼴
    # 4-3. cv2.FONT_HERSHEY_DUPLEX: 산세리프체 진한 글꼴
    # 4-4. cv2.FONT_HERSHEY_COMPLEX_SMALL: 세리프체 작은 글꼴
    # 4-5. cv2.FONT_HERSHEY_COMPLEX: 세리프체 일반 글꼴
    # 4-6. cv2.FONT_HERSHEY_TRIPLEX: 세리프체 진한 글꼴
    # 4-7. cv2.FONT_HERSHEY_SCRIPT_SIMPLEX: 필기체 산세리프 글꼴
    # 4-8. cv2.FONT_HERSHEY_SCRIPT_COMPLEX: 필기체 세리프 글꼴
    # 4-9. cv2.FONT_ITALIC: 이탤릭체 플래그
# 5. fontSize : 글꼴 크기
# 6. color : 선 색상, (Blue, Green, Red), 0 ~ 255
# (생략가능) 7. thickness=1:  선 두께 (-1: 색으로 꽉 채우기)
# (생략가능) 8. lineType: 선 그리기 형식 (cv2.LINE_4: 4연결 선 알고리즘, cv2.LINE_AA: 안티에일리어싱-> 계단현상없음)



# sans-serif small
cv2.putText(img, "Plain", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,0))
# sans-serif normal
cv2.putText(img, "Simplex", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0,0))
# sans-serif bold
cv2.putText(img, "Duplex", (50, 110), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0,0))
# sans-serif normall X2
cv2.putText(img, "Simplex", (200, 110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,250))

# serif small
cv2.putText(img, "Complex Small", (50, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0,0))
# serif normal
cv2.putText(img, "Complex", (50, 220), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0,0))
# serif bold
cv2.putText(img, "Triplex", (50, 260), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0,0))
# serif normal X2
cv2.putText(img, "Complex", (200, 260), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,255))

# hand-wringing sans-serif
cv2.putText(img, "Script Simplex", (50, 330), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 0,0))
# hand-wringing serif
cv2.putText(img, "Script Complex", (50, 370), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0, 0,0))

# sans-serif + italic
cv2.putText(img, "Plain Italic", (50, 430), cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC, 1, (0, 0,0))
# sarif + italic
cv2.putText(img, "Complex Italic", (50, 470), cv2.FONT_HERSHEY_COMPLEX | cv2.FONT_ITALIC, 1, (0, 0,0))

cv2.imshow('draw text', img)
cv2.waitKey()
cv2.destroyAllWindows()