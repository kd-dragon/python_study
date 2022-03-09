import numpy as np

x = np.arange(0,10)
y = np.arange(10,20)
z = np.arange(20,30)

np.savez('arange.npz', array1=x,array2=y,array3=z)
data = np.load('arange.npz')

result1 = data['array1']
result2 = data['array2']
result3 = data['array3']

print(result1,result2,result3)

array1 = np.arange(0,10)
array2 = np.copy(array1)
array2[0] = 1004

print (array1)
print (array2)