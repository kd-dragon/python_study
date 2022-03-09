#subplot
# plt.plot() 함수를 여러번 호출하면 하나의 다이어그램에 겹쳐져서 그래프가 나타난다.
# ex) subplot(행,열,몇번째)
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
plt.subplot(2,2,1)  #2행 2열 중에 1번째
plt.plot(x,x**2)
print(x)
print(x**2)

plt.subplot(2,2,2)  #2행 2열 중에 2번째
plt.plot(x,x*5)

plt.subplot(2,2,3)    #2행 2열 중에 3번째
plt.plot(x, np.sin(x))

plt.subplot(2,2,4)    #2행 2열 중에 4번째
plt.plot(x, np.cos(x))

plt.show()