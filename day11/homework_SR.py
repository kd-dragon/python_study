sample_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]
sample_list2 = ['a','b','c','b','b','d','e','f','f','서륭','대용','광호','광호','대용','서륭','z','z','a','a','a',]

s1 = list(set(sample_list))
s2 = list(set(sample_list2))

print(s1)
print(s2)

# ---------------------------------------------
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 3, 5, 7, 9, 11, 13]
c = [0, 11, 12, 5, 3, 7]

a1 = set(a)
b1 = set(b)
c1 = set(c)

x1 = list(a1 & b1 & c1) #AND 교집합
x2 = list(a1 | b1 | c1) #OR 합집합

print(x1)
print(x2)