def gugudan(num):
    for n in range(2, 10):
        mul = n * num
        print("{} x {} = {}" .format(n, num, mul), end="\t\t")
    print()
    if 0 < num < 9:
        num += 1
        gugudan(num)
    else:
        print("Finish !")


gugudan(2)