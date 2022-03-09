import cv2

img = cv2.imread('blank_img.jpg')

for i in range(0,10):
    cv2.circle(img,(100+i,100+i),90+i,(255+i,0,0))
    cv2.circle(img,(200+i,200+i),70+i,(0,255+i,0))
    cv2.circle(img,(300+i,300+i),50+i,(0,0,255+i))
    cv2.circle(img,(400+i,400+i),30+i,(255+i,0+i,0+i))
    cv2.circle(img,(450+i,450+i),10+i,(0+i,255+i,0+i))

cv2.imshow('circle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()