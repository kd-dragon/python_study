abcde_list = ['a', 'b', 'c', 'd']
print(abcde_list)
print(id(abcde_list))

abcde_list.append('e')

print(abcde_list)
print(id(abcde_list))

abcde_list.pop()

print(abcde_list)
print(id(abcde_list))

dics = {'a': 1}
print(dics)
print(id(dics))

dics['b'] = 2
print(dics)
print(id(dics))

del dics['b']
print(dics)
print(id(dics))
