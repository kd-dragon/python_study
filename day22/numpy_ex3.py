import numpy as np
import math as mt

# Numpy 주 활용 코드

ar1 = np.arange(0, 10)
ar2 = np.arange(10, 20)

np.savez('save1.npz', array1=ar1, array2=ar2)
result = np.load('save1.npz')

data1 = result['array1']
data2 = result['array2']

####################################

# linspace : 균일한 간격으로 데이터 생성
array = np.linspace(0, 10, 5) # 0부터 10사이에 5개 값을 만들기!
# print(array)

# Numpy 배열을 복제하기
a = np.arange(0, 10)
b = a.copy()
b[0] = 1000

# Numpy 중복된 원소 제거
duple = np.array([6, 6, 6, 6, 6, 6, 6,1,1,2,2,2,3,3,3,3,3,3,3,4,5,5,5,5])
# print(np.unique(duple))

# 행렬 데이터 다루기
# 1) 평균값
ex1 = np.array([1,3,4,6,8,9, 10 ,11,76,346,12344])
# print(np.mean(ex1))

# 2) 중앙값
ex2 = np.array([1, 3, 4, 6, 8, 9, 10, 11, 76, 346, 12344])
# print(np.median(ex2))

# 3) 표준 편차 && 분산
# 편차 ? 평균값 기준 차이
# -15, -5, +5, +15
# 15 + 5 + -5 + -15 = 0 편차의 합은 0이므로 평균값을 구할수가 없다...
# 어떻게하면 편차의 평균을 구할수일까??? 음수값을 양수로 바꾸면 되지않을까????
# 모든 편차들을 제곱해서 평균을 내자! (=> 분산)
# 제곱을 했으니 다시 루트를 씌우자 !! (=> 표준편차)


ex3 = np.array([160, 170, 180, 190]) # -15, -5, +5, +15
x = np.mean(ex3)

tmp = (-15)**2 + (-5) **2 + 5**2 + 15 **2
print(tmp / 4)
print(mt.sqrt(tmp/4))

print(np.std(ex3))
print(np.var(ex3))