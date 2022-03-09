a_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

for a in a_list:

    for b in a:

        if b < 15:

            print(b, end=",")

        elif b == 15:

            print(b)

print("\n")

for a in a_list[::-1]:
    for b in a[::-1]:

        if 1 < b <= 15:

            print(b, end=",")

        elif b == 1:

            print(b)
    print()
print("\n")

for a in range(0, 5):

    for b in range(0, 5):

        if b < 4:

            print('*', end="")

        elif b == 4:

            print('*')

print("\n")

for a in range(0, 5):

    s = '*'

    for b in range(0, a + 1):

        if b < a:

            print(s, end="")

        elif b == a:

            print(s)

print("\n")

for a in range(0, 5):

    s = '*'

    for b in range(4, -1, -1):
        if b > a:
            print(s, end="")
        elif b == a:
            print(s)

