def add_drink():
    print('음료목록:', drinklist)
    adddrink = input('추가할 음료는?')
    drinklist.append(adddrink)
    print('음료목록', drinklist)
    print('---------------------------------')


def del_drink():
    print('음료목록:', drinklist)

    deldrink = input('삭제할 음료는?')
    i = drinklist.index(deldrink)
    del drinklist[i]

    print(drinklist)
    print('---------------------------------')


def japangi():
    money = int(input('동전을 넣으세요(500원이상):'))
    print('(현제 금액:', money, '원)', '음료목록:', drinklist)

    while money >= 0:
        selectdrink = int(input('음료를 선택하세요(순서대로 1,2,3... 입력, 거스름돈 받기:0):'))

        if selectdrink > 0:
            # selectdrink -= 1
            # i = drinklist.index(drinklist[selectdrink - 1])

            print(drinklist[selectdrink - 1], '가 나왔습니다')
            change = money - 500
            if change >= 0 :
                print('(현재 금액:', money - 500, '원)', '음료목록:', drinklist)

            money -= 500
            if money < 500:
                print('돈이 없습니다')
                break

        elif selectdrink == 0:
            print('거스름돈은', money, '원 입니다.')
            print('처음부터 다시 시도해주세요')
            print('---------------------------------')
            break


def closeprogram():
    print('자판기 관리 프로그램 종료')


drinklist = []
money = 0

while True:
    # 메인 소스
    print('@@@@@@@@@시스템가동 준비완료@@@@@@@@@')
    print('1: 음료추가 2: 음료삭제 3: 자판기이용 4: 종료')
    inputdata = input('기능선택:')

    if inputdata == '1':
        add_drink()

    elif inputdata == '2':
        del_drink()

    elif inputdata == '3':
        japangi()

    elif inputdata == '4':
        closeprogram()
        break
    else : print('없는 기능 입니다.')