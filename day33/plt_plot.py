import matplotlib.pyplot as plt
import numpy as np

# 1차원 배열 테스트 (x축:인덱스, y축: 값)
# plot() -> 그래프를 그리는 가장 간단한 함수
# a = np.array([2,6,7,3,103,8,4,5])    # 배열 생성
# plt.plot(a)                         # plot 생성
# plt.show()                          # plot 그리기


# 두 배열의 상관관계
x = np.arange(10)  # [0,1,2,3,4,5,6,7,8,9]
y = x**2   # [0,1,4,9,16,25,36,49,64,81]

# y=x^2

plt.plot(x,y)      # plot 생성
plt.show()         # plot 화면에 표시