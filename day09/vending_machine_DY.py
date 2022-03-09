# 자판기 관리 프로그램
import time
import tqdm as tq

drink_list = ['사이다', '콜라']

# 부가기능 (시간 딜레이)
def delay_time():
    count = 5
    # count 부터 0까지 -1씩 증감하는 for 문
    for x in range(count, 0, -1):
        print(".", end="")
        time.sleep(1)
    print("\n\n\n\n\n")


# 부가기능 (프로그레스바)
def percent_gauge():
    total = 0
    for x in tq.tqdm(range(100), ncols=100, desc="프로그램 시작 ="):
        time.sleep(0.001)
        total += x
    print(total)

# 부가 기능 (메시지 출력폼)
def msg_form(msg):
    print('###################################################################')
    #print('{:^67}'.format(msg))
    print(msg.center(68, ' '))
    print('###################################################################')
    print()


# 메인 기능 (음료 추가)
def add():
    drink_name = input('추가할 음료 이름을 입력하세요 : ')

    if drink_name is not None and drink_name.strip() != "":
         drink_list.append(drink_name)
         msg_form("[성공] 새로운 음료 등록 완료")

    else:
        msg_form("잘못된 입력")


# 메인 기능 (음료 제거)
def delete():
    while True:
        try:
            drink_num = int(input('삭제할 음료 번호를 입력하시오 : '))
            del drink_list[drink_num-1]
            msg_form("[성공] 음료가 제거되었습니다.")
            break
        except ValueError:
            msg_form("[실패] 번호만 입력해주세요")

        except IndexError:
            msg_form("[실패] 메뉴판에 없는 번호")


# 메인 기능 (음료 목록 출력)
def print_menu():
    print('\n\n')
    print('# 자판기 메뉴판 # ')
    if len(drink_list) == 0:
        print('현재 등록된 음료가 없습니다.')
    else:
        for num in range(len(drink_list)):
            print("({num}){name}".format(num=num + 1, name=drink_list[num]), end=" | ")
        print()


# 메인 기능 (자판기 메인 기능)
def use_machine(init_money):
    # 자판기에 돈넣기
    total_money = charge_money(init_money)
    # 메뉴판 보여주기
    print_menu()
    # 메뉴 고르기
    select_menu(total_money)


# 메인 기능 (자판기 돈 넣기)
def charge_money(init_money):

    total_money = init_money

    while True:
        try:
            input_money = int(input('돈을 넣어주세요 (1000원, 500원, 100원만 허용): '))

            if (input_money % 100 != 0):
                msg_form("[실패] 화폐 인식 불가 (정해진 화폐만 넣어라....)")

            elif input_money < 0:
                msg_form("[실패] 화폐 인식 불가 (음수따위 없다....)")

            else:
                total_money += input_money
                msg_form("현재 금액: {money}".format(money=total_money))

                key = input('계속 돈을 넣으시려면 엔터키를 누르시고, 주문하시려면 아무 키나 입력해주세요.')
                if key != '':
                    break
        except ValueError:
            msg_form("[실패] 화폐 인식 불가")
    return total_money


# 메인 기능 (음료 고르기)
def select_menu(total_money):
    change_money = 0

    while True:
        try:
            drink_num = int(input('음료 번호를 입력하시오 : '))
            drink_name = drink_list[drink_num - 1]

            change_money = total_money - 500
            if change_money == 0:
                msg_form("[성공] {name}가 나왔습니다. 맛있게 드세요~".format(name=drink_name))
                print('[거스름돈: {change}원] 자판기 프로그램이 초기화 됩니다.'.format(change=change_money))
                delay_time()
                break
            elif change_money > 0:
                msg_form("[성공] {name}가 나왔습니다. 맛있게 드세요~".format(name=drink_name))
                key = input('[잔돈: {change}원] 계속 주문하시려면 엔터키를 누르시고, 주문을 종료하시려면 아무키나 입력해주세요. '.format(change=change_money))
                if key != '':
                    print('주문이 취소되었습니다. [거스름돈: {change}원]을 받아가시기바랍니다.'.format(change=change_money))
                    break
            else:
                print('잔돈이 부족합니다. 돈을 더 넣어주시기바랍니다.')
                use_machine(total_money)
                break

            total_money = total_money - 500
        except ValueError:
            msg_form("[실패] 번호만 입력해주세요")

        except IndexError:
            msg_form("[실패] 메뉴판에 없는 번호")


# ================================ Main 프로그램 소스 ======================================
msg_form("VENDING MACHINE PROGRAM IS RUNNING !!! [Made By DaeYong]")
percent_gauge()

# 메인 반복문
while True:
    print_menu()

    print('=========================== [기능 목록] =============================')
    print('|   [1]음료추가   |   [2]음료삭제   |   [3]자판기이용   |   [4]종료     |')
    print('===================================================================')

    order = input('기능선택: ')

    if order == '1':
        # 음료추가 함수 호출
        add()
    elif order == '2':
        # 기능 2번 구현
        delete()
    elif order == '3':
        # 기능 3번 구현
        use_machine(0)
    elif order == '4':
        print('================= 자판기 관리 프로그램 종료 =================')
        break



