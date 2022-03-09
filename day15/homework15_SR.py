for i in range(1,10):

    for a in range(2,10):

        d = i*a

        if d >= 10:
            print(a,'*',i,'=',i*a, end='  ')

        elif d <= 10:
            print(a, '*', i, '=', i * a," ", end=' ')
    print()


for i in range(5,0,-1):
    print(' '*(5-i), "*"*(2*i-1))

