
drink_dic = {}
drink_dic['콜라'] = 1000
drink_dic['사이다'] = 2000
drink_dic['환타'] = 1500
print(drink_dic)

if '콜ㅇ라' in drink_dic:
  print(drink_dic['콜라'])
else:
  print('없음')

drink_dic.pop('콜라')
print(drink_dic)

