import numpy as np
arr = np.arange(10000)
list = arr.tolist()
print(arr * 2)

a = []

for i in list:
    a.append(i * 2)
print(a)