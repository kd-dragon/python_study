# 10부터 0까지 카운트를 세고 0이되면 Boom! 이라는 문자열을 출력하는 함수를 만드시오.
# 매개변수로 카운트 시작 숫자를 받으시오

def countdown(n):
    for k in range(n, 0, -1):
        print(k)
    else:
        print("Boom !")


countdown(10)