for i in range(1, 10):

    for s in range(2, 10):

        a = i * s

        if a < 10:

            print(s, "*", i, "=", "", a, end="    ")

        elif a >= 10:

            print(s, "*", i, "=", a, end="    ")

    print("")

for a in range(0, 5):

    s = '*'
    i = [18, 14, 10, 6, 2]
    ss = ''

    for b in range(1, i[a], 2):

        if round(b % 2) == 1:
            ss += s

    print(ss.center(10), end="")
    ss = ''
    print()
