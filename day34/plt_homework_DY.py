import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

img_list = []
PATH = os.path.dirname(os.path.abspath(__file__))
dir_name = os.path.join(PATH, "imgs")

file_list = os.listdir(dir_name)

print(dir_name)
print(file_list)
for x in file_list :
    if x.endswith(".jpg"):
        print(x)
        print(os.path.join(dir_name, x).replace("\\","/"))
        # img_list.append(cv2.imread(os.path.join(dir_name, x).replace("\\","/")))

# C:/Users/KDY/Desktop/파이썬/dailyQuiz/day34/imgs/1.jpg

#### cv.imread, write시 한글 인식 문제
img_array = np.fromfile("C:/Users/KDY/Desktop/파이썬/dailyQuiz/day34/imgs/1.jpg", np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)  #decode : 해독, 복호화 <-> encode

plt.imshow(img[:,:,::-1])
plt.xticks([])
plt.yticks([])
plt.show()
