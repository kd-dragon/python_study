import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(1,6)

# 1. marker, linestyle, color
# 2. string format 활용하여 스타일 지정
#plt.plot(x,x,".-r")   # 1.
#plt.plot(x,x+1,"^--g") # 2.
#plt.plot(x,x+2, "*-.r") # 3.
#plt.show()

x = np.arange(10)
f1 = x * 5
f2 = x **2
f3 = x **2 + x*2

plt.plot(x,'r--')   # 빨강색 이음선
plt.plot(f1, 'g.')  # 초록색 점
plt.plot(f2, 'bv')  # 파랑색 역 삼각형
plt.plot(f3, 'ks' ) # 검정색 사각형
plt.show()
