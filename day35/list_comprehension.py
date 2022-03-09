# List Comprehension

# 파이썬의 리스트는 리스트 안에 for 반복문과 if 조건문을 사용할 수 있다.
c = list(range(5, 20))
# 1) 기본 구문
a = [i for i in range(10)]
b = list(i for i in range(10))

# 2) 결과에 연산을 더하기
c = [i ** 2 for i in range(10)]
d = list(i + 1000 for i in range(10))

# 3) if 조건문 사용
e = [i for i in range(10) if i % 2 == 0]
print(e)

dan = 3
# 4) for 반복문을 여러번 사용하기
gugudan = [x*i for x in range(2, 15) if x == dan for i in range(1, 10)]
print(gugudan)




# 복합 연습문제
 # 0~9 숫자 중 홀수에 5를 더하여 리스트 생성하시오!
 # list 함수를 쓰세요~