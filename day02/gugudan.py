# 구구단의 단을 입력하면 해당 단을 출력해주는 함수를 만드시오.
# 힌트: input 함수 사용, 문자열로 계산 안되도록 int 형으로 변환 필요
# t = int(input("출력할 단을 입력하세요 : "))

def gugudan(num):
    for n in range(9):
        mul = int(n+1) * num
        print("{} x {} = {}" .format(num, n+1, mul))


print("[구구단 프로그램]")
t = int(input("출력할 단을 입력하세요 : "))
gugudan(t)