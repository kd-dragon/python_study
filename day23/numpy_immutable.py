import numpy as np
array1 = np.arange(0 ,10)
array2 = array1
array2[0] = 99
print(array1)
#array2 = array1.copy()
#print(array2)

#리스트
list1 = [0,1,2,3,4,5]
list2 = list1
list2[0] = 90
print(list1)

#딕셔너리
dic1 = {"a":1,"b":2,"c":3}
dic2 = dic1
dic2["a"]=99
print(dic1)



# immutable
#String
str1 = "0,1,2,3,4,5"
str2 = str1


#튜플
tuple1 = (0,1,2,3,4,5)
tuple2 = 0

print("########")
print(tuple1[0])
tuple2 = tuple1[0]
print(tuple1)
print("########")