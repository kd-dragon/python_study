import numpy as np
import copy

x= np.arange(0, 10)
y = np.arange(10, 20)
z = np.arange(30, 40)


np.savez('saved.npz', array1=x, array2=y, array3=z)
data = np.load('saved.npz')
result1 = data['array1']
result2 = data['array2']
result3 = data['array3']

print(result1,result2,result3)



print('--------------------------------------------------')

array1 = np.arange(0, 10)  #배열 생성
array2 = np.copy(array1)
# array2 = array1
array2[0] = 1004


print(array1)
print(array2)