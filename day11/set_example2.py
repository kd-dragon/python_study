# 2) set 을 사용해서 주어진 리스트들로 원하는 값을 출력하시오.
#  2-1. 다음 3개의 리스트의 교집합을 출력하시오.
#  2-2. 다음 3개의 리스트의 합집합을 출력하시오.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 3, 5, 7, 9, 11, 13]
c = [0, 11, 12, 5, 3, 7]

a_set = set(a)
b_set = set(b)
c_set = set(c)



print(a_set.intersection(b_set).intersection(c_set))