class PocketMon:
    # 포켓몬 객체 생성시 속성 만들고 초기화~
    def __init__(self):
        self.num = ""
        self.name = ""
        self.hpoint = 0
        self.attack = 0
        self.defence = 0
        self.speed = 0


# 포켓몬 5마리 생성~~~~
pocket1 = PocketMon()
pocket2 = PocketMon()
pocket3 = PocketMon()
pocket4 = PocketMon()
pocket5 = PocketMon()

# 안에있는 속성이나 메소드는 . 키로 접근할 수 있음
# 속성값 출력해보자
print(pocket1.num)
print(pocket1.name)
print(pocket1.hpoint)
print(pocket1.attack)
print(pocket1.defence)
print(pocket1.speed)

print("===============================================================")
# 자 이제 포켓몬을 정의하자 (pocket1과 같이 나머지 들도 정의)
pocket1.num = 1
pocket1.name = "피카츄"
pocket1.hpoint = 50
pocket1.attack = 61
pocket1.defence = 32
pocket1.speed = 70

# 다시 출력해보자~
print(pocket1.num)
print(pocket1.name)
print(pocket1.hpoint)
print(pocket1.attack)
print(pocket1.defence)
print(pocket1.speed)

print("===============================================================")
# 제대로 만들어졌으니 pocket1을 리스트에 담자

pocket_list = []
pocket_list.append(pocket1)

# 리스트를 출력해보자
print(pocket_list)

print("===============================================================")
# 리스트 안에 포켓몬 정보를 출력해보자
for a in pocket_list:
    print(a)
    print(a.num)
    print(a.name)
    print(a.hpoint)
    print(a.attack)
    print(a.defence)
    print(a.speed)



