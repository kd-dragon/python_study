import os

PATH = os.path.dirname(os.path.abspath(__file__))
dir_name = 'imgs'
full_path = os.path.join(os.path.dirname(__file__), dir_name)

print("==============================================")
print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))
print(full_path)

print(os.path.split(__file__))
rtn = os.path.split(__file__)
print(rtn[0])
print(rtn[1])
print(os.path.splitext(rtn[1]))
rtn2 = os.path.splitext(rtn[1])

if rtn2[1] == ".jpg" :
    print("OK")

# os.path.split()  : 파일디렉토리/파일명 분리
# os.path.splitext() : 파일명/확장자 분리



