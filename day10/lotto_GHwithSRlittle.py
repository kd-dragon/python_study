import time
import random

prize_num = []

rotto_num = []
money_box = 0
buy_count = 0


def delay_time(num):
    count = num
    # count 부터 0까지 -1씩 증감하는 for 문
    for x in range(count, 0, -1):
        time.sleep(1)
    print("\n")


def rotto_pickNum(a):
    rotto_range = list(range(1, 46))

    for i in range(a):
        num = random.sample(rotto_range, 6)
        num.sort()
        rotto_num.append(num)
        print("결과 :", num)
        print("\n")


def input_coin():  ###### 자판기 이용
    global money_box

    while True:

        try:
            a = int(input('돈을 넣으세요( 장당 1000원[지폐만ㅎㅎ]):'))

            if a <= 999:

                print("\n\n")
                print("1000원 이상만 넣어주세요!")
                print("\n")

            elif a % 1000 > 0:

                print("\n\n")
                print("천원 단위로 넣어주세요~")
                print("\n")

            else:

                break

        except ValueError:
            print("\n\n")
            print('잘못된 입력입니다. (문자사용).')
            delay_time(1)
            a = 0
            break

    money_box += a

    print("\n\n")
    print("(", "현재 금액:", money_box, ")")
    print("\n")


def buy_rotto():
    global money_box
    global buy_count
    price = 1000

    while True:

        a = int(input("몇 장 사시겠습니까?"))

        buy_count = a

        if price * a <= money_box:

            money_box -= price * a

            print(a, "장 구매 하셨습니다.")
            print("\n")

            rotto_pickNum(a)

            print("거스름돈", money_box, "원")

            money_box == 0

            break

        elif a <= 0:
            print("1장 이상 구매해 주세요")


def check_rotto(buy_count):
    count = buy_count

    a = int(input("첫번째 번호 입력"))
    prize_num.append(a)
    print(prize_num)

    b = int(input("두번째 번호 입력"))
    prize_num.append(b)
    print(prize_num)

    C = int(input("세번째 번호 입력"))
    prize_num.append(C)
    print(prize_num)

    d = int(input("네번째 번호 입력"))
    prize_num.append(d)
    print(prize_num)

    e = int(input("다섯번째 번호 입력"))
    prize_num.append(e)
    print(prize_num)

    f = int(input("여섯번째 번호 입력(마지막)"))
    prize_num.append(f)
    print(prize_num)

    print("\n")

    for i in range(count):

        print(i + 1, "번째 결과")

        print(set(rotto_num[i]).intersection(prize_num))
        matchingNum = len(set(rotto_num[i]).intersection(prize_num))

        if matchingNum == 6:
            print("=> [1등] 6개가 다 맞았습니다!!!")
            print("\n")
        elif matchingNum == 5:
            print("=> [2등] 5개가 맞았습니다!!!")
            print("\n")
        else:
            print("=> 꽝입니다.")
            print("\n")


def dice():
    # print(random.randrange(1, 7))
    x = random.randrange(1, 7)
    print(x)
    if x == 1:
        print('하나')
    elif x == 2:
        print('둘')
    elif x == 3:
        print('셋')
    elif x == 4:
        print('넷')
    elif x == 5:
        print('다섯')
    else:
        print('여섯')


    # print(random.choice(['하나', '둘', '셋', '넷', '다섯', '여섯']))


def lotto():
    i = random.sample(range(1, 46), 6)
    i.sort()
    print(i)


while True:

    print("======================기능==============================")
    print()
    print("1: 로또사기 2: 당첨확인 3: 주사위 굴리기 4: 로또 당첨번호 추출 5: 종료")
    print()
    print("========================================================")

    inputdata = input('기능선택 : ')

    if inputdata == '1':
        input_coin()
        buy_rotto()



    elif inputdata == '2':
        check_rotto(buy_count)


    elif inputdata == '3':
        print("뿅!")
        dice()

    elif inputdata == '4':
        lotto()

    elif inputdata == '5':
        print("종료됩니다.....")
        break

    else:
        print("\n\n")
        print("없는 옵션인'대용'?")


