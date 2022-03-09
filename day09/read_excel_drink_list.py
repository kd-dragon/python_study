import openpyxl as xls

workbook = xls.load_workbook('drink_list.xlsx')
sheet = workbook['Sheet1']

#cell_range = sheet['A':'B']
#row_range = sheet[1:sheet.max_row]

cell_range = sheet.columns
row_range = sheet.rows

def get_drink_list():
    # 행 기준 열 출력
    row_list = []
    for col in row_range:
        print()
        for cell in col:
            row_list.append(cell.value)
            print(cell.value, end=", ")
    print()
    print(row_list)


    # 열 기준 행 출력
    list_var = []

    for row in cell_range:
        print()
        for cell in row:
            list_var.append(cell.value)
            print(cell.value, end=", ")
    print()
    print(list_var)

    return row_list


def get_drink_dic():

    # 행 기준 열 출력
    drink_dic = {}
    key = ""
    isOdd = 0

    for col in row_range:
        for cell in col:
            isOdd += 1
            if isOdd % 2 != 0:
                key = cell.value
            else:
                drink_dic[key] = cell.value

    print(drink_dic)
    return drink_dic

