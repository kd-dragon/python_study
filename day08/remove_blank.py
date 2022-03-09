
f1 = open("address.txt", 'r', encoding='utf-8')
data = f1.read()

print(data)
print("====================== 코딩 후 ========================== ")

temp_data = data.replace(" ", "").replace("\t", "")
print(temp_data)