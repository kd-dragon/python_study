import os

PATH = os.path.dirname(os.path.abspath(__file__))
#dir_name = os.path.join(PATH, "imgs")
dir_name = "./imgs"
#C:/Users/KDY/Desktop/파이썬/dailyQuiz/day34\imgs

# 특정 디렉토리에서 여러 파일 가져오기

# 1) os.listdir()
imgs = os.listdir(dir_name)
print(imgs)

print("================================================")

# 2) os.walk()
for path, dirs, files in os.walk(dir_name):
    print(path.replace("\\","/"), dirs, files)




