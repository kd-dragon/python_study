import openpyxl as xls

workbook = xls.load_workbook('pockemon.xlsx')
sheet = workbook['Sheet1']

cell_range = sheet.columns
row_range = sheet.rows

pocket_list = []

class PocketMon:

    def set_data(self, num, name, hpoint, attack, defence, speed):
        self.num = num
        self.name = name
        self.hpoint = hpoint
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.sum = self.hpoint + self.attack + self.defence + self.speed

    def set_sum(self):
        self.sum = self.hpoint + self.attack + self.defence + self.speed

    def print_data(self):
        print(self.num, end=" | ")
        print(self.name, end=" | ")
        print(self.hpoint, end=" | ")
        print(self.attack, end=" | ")
        print(self.defence, end=" | ")
        print(self.speed, end=" | ")
        print(self.sum)

    def __init__(self):
        self.num = ""
        self.name = ""
        self.hpoint = 0
        self.attack = 0
        self.defence = 0
        self.speed = 0
        self.sum = 0

test = PocketMon()

def get_pockemon_by_row():
    # 행 기준 열 출력
    row_list = []
    #row_range = [[1, 피카츄, 60, 40, 34, 60], [2, 파이리, 70, 41, 56, 32], [3, 꼬부기, 73, 36, 67, 43]]
    for col in row_range:

        #col >[1, 피카츄, 60, 40, 34, 60]
        is_appendable = True
        pocket_mon = PocketMon()
        print("================ 다음 행 ===================")
        for cell in col:

            if cell.column == 1:
                # 변수 오브젝트 유형(type) 비교
                if isinstance(cell.value, int):
                    pocket_mon.num = cell.value
                else:
                    is_appendable = False
                    break

            elif cell.column == 2:
                pocket_mon.name = cell.value
            elif cell.column == 3:
                pocket_mon.hpoint = cell.value
            elif cell.column == 4:
                pocket_mon.attack = cell.value
            elif cell.column == 5:
                pocket_mon.defence = cell.value
            elif cell.column == 6:
                pocket_mon.speed = cell.value
            else:
                continue

        # 리스트에 추가 여부 확인
        if is_appendable:
           row_list.append(pocket_mon)

    print()
    print(row_list)
    return row_list

def print_all():
    for obj in pocket_list:
        obj.print_data()

def search():

    keyword = ""
    try:
        keyword = input("찾을 포켓몬의 '번호' 또는 '이름'을 입력해 주세요!!! [현재 {0}종 ]  ".format(len(pocket_list) - 1))

        # 키워드 정수로 형변환
        keyword = int(keyword)

        for obj in pocket_list:
            if obj.num == keyword:
                obj.print_data()
                return

    except ValueError:
        # 정수 형변환시 오류 발생하면 이름으로 검색했다고 판별
        for obj in pocket_list:
            if keyword in obj.name:
                obj.print_data()


def string_weak():
    sum_list = []
    strong_val = 0
    weak_val = 0

    for obj in pocket_list:
        obj.set_sum()
        sum_list.append(obj.sum)

    print("[가장 쎈 포켓몬] ", end="")
    print("Strong Point :: ", max(sum_list))
    strong_val = max(sum_list)

    for obj in pocket_list:
        if obj.sum == strong_val:
            obj.print_data()

    print("[가장 약한 포켓몬] ", end="")
    print("Week Point :: ", min(sum_list))
    weak_val = min(sum_list)

    for obj in pocket_list:
        if obj.sum == weak_val:
            obj.print_data()



# ==========================================================

pocket_list = get_pockemon_by_row()

while True:

    # 프로그램 실행
    print()
    print()
    print()
    print("======================기능==============================")
    print()
    print("1: 포켓몬 전체확인  2: 포켓몬 검색  3: 가장 쎈 포켓몬과 가장 약한 포켓몬 출력  4: 종료 ")
    print()
    print("========================================================")

    inputdata = input('기능선택 : ')

    if inputdata == '1':
        print_all()

    elif inputdata == '2':
        search()

    elif inputdata == '3':
        string_weak()

    elif inputdata == '4':
        print()
        print('종료')
        print()
        break

    else:
        print("\n\n")
        print("없는 옵션인'대용'?")