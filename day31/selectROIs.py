import cv2

img = cv2.imread('test.jpg')

recs = cv2.selectROIs('img', img, False)

print("recs = ", recs)

for r in recs:
    print(f'r:{r}')
    # x, y, w, h
    cv2.rectangle(img, (r[0], r[1]), (r[0]+r[2], r[1]+r[3]), 255)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()