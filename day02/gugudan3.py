#구구단 2단부터 9단까지 한번에 출력하는 함수를 만드시오
#함수의 인자를 가변인자 형태로 넘겨주세요. 힌트( 파라미터: * args, 인자: 2,3,4,5,6,7,8,9)
#아래 출력과 동일하게 출력해주세요. 힌트 (print 함수의 end 사용)


def gugudan_all2(*args):
    for n in range(9):
        for dan in args:
            mul = int(n+1) * dan
            print("{} x {} = {}".format(dan, n + 1, mul), end='\t')
        print("")


print("[구구단 출력 프로그램]")
gugudan_all2(2, 3, 4, 5, 6, 7, 8, 9)