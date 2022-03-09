import csv

f = open('csvtest2.csv', 'w', newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(['첫번째', '두번째', '세번째', '네번째', '다섯번째']) # 리스트
csv_writer.writerow(['1','2','3','4','5'])

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

list_all = [list1, list2, list3]
for x in list_all:
    csv_writer.writerow(x)

f.close()
