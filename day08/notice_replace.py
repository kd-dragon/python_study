
f1 = open("notice.txt", 'r', encoding='utf-8')
data = f1.read()

output = data.replace("#{이름}", "김대용")\
    .replace("#{상품명}", """한우 A세트""")\
    .replace("#{날짜}", "2020년 11월 15일 18시경")\
    .replace("#{전화번호}", "02-123-4567")

print(output)