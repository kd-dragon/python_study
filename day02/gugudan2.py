
#구구단 2단부터 9단까지 한번에 출력하는 함수를 만드시오
#함수의 인자를 list 형태로 넘겨주세요. ex) dan_list = [2, 3, 4, 5, 6, 7, 8, 9]
#힌트: 2중 for문 사용 -> for문 안에 for문.
#아래 출력과 동일하게 출력해주세요. 힌트 (print 함수의 end 사용)


def gugudan_all(d_list):
    for n in range(1, 10):
        for dan in d_list:
            mul = n * dan
            print("{} x {} = %3d".format(dan, n) % mul, end='\t\t')
        print("")


print("[구구단 출력 프로그램]")
dan_list = [2, 3, 4, 5, 6, 7, 8, 9]
gugudan_all(dan_list)


