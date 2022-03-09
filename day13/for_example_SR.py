a_list = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
for i in a_list:
    for x in i:
        print(x,end=',')

print()
print()

a_list = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

print(a_list)

for i in a_list:
    i.reverse()
    for x in i:
        print(x,end=',')

print()
print()

for i in range(5):
    for x in range(5):
        print('*',end='')

    print()

print()

for i in range(0, 5):
    for x in range(0,i+1):
        print('*',end='')
    print()

print()


for i in range(0, 5):
    for x in range(5,i,-1):
        print('*',end='')
    print()
