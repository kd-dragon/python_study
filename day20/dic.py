

dic = {}

dic[1] = '대용'
dic['1'] = '서륭'
dic['대용'] = 1
dic[1] = '광호'


print(dic[1])  #대용
print(dic['1']) #서륭
print(dic['대용'])

print(dic)

for key, value in dic.items():
    print(key)