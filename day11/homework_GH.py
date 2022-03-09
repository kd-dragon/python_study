#1) set을 사용해서 주어진 리스트의 중복데이터가 제거된 리스트를 만드시오.
# 최종 type은 list여야합니다.

sample_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]
sample_list2 = ['a','b','c','b','b','d','e','f','f','서륭','대용','광호','광호','대용','서륭','z','z','a','a','a',]


sl = list(set(sample_list))
sl2 = list(set(sample_list2))

print(sl)
print(sl2)



# 2) set 을 사용해서 주어진 리스트들로 원하는 값을 출력하시오.
#  2-1. 다음 3개의 리스트의 교집합을 출력하시오.
#  2-2. 다음 3개의 리스트의 합집합을 출력하시오.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 3, 5, 7, 9, 11, 13]
c = [0, 11, 12, 5, 3, 7]

intersec = list(set(a).intersection(b).intersection(c))
union = list(set(a).union(b).union(c))

print(intersec)
print(union)