class Person:
    def __init__(self, p_name, p_age):
        self.name = p_name
        self.age = p_age

    def out(self):
        print("이름: " + self.name + " | 나이: " + str(self.age))


p1 = Person("홍길동", 20)  # Person 인스턴스(객체) 생성하여 p1에 넣는다. (인스턴스 생성시 __init__ 함수가 수행되어 이름이 홍길동, 나이가 20으로 초기화 된다)
p2 = Person("김대용", 30)  # Person 인스턴스(객체) 생성하여 p2에 넣는다.

print(p1.age)  # p1의 age 변수 값을 출력
print(p2.age)  # p2의 age 변수 값을 출력
print(p1.name)  # p1의 name 변수 값을 출력
print(p2.name)  # p2의 name 변수 값을 출력

# id 값을 확인하여 서로 다른 인스턴스(객체)임을 확인해보자.
print(id(p1)) # p1의 id 값을 출력
print(id(p2)) # p2의 id 값을 출력

# 객체 내 함수 out 을 호출한다.
p1.out()
p2.out()