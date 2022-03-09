

for a in range(0,5):

    s = '*'
    i = [2,6,10,14,18]
    ss = ''

    for b in range(1,i[a],2):


        if round(b % 2) == 1:

        
            ss += s
    
    print(ss.center(10),end="")
    ss = ''
    print()


