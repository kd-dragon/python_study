print(dir(str))
f1 = open("address.txt", 'r', encoding='utf-8')
data = f1.read()

temp_data = data.replace(" ", "").replace("\t", "").split()
output = []

for info in temp_data:
    rslt = ''

    for idx in range(len(info)):
        if info[idx].isdigit():
            rslt = info[:idx] + ":" + info[idx:]
            output.append(rslt)
            break

print()
print(output)