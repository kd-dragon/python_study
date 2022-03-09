def write_lines(line_num, path):
    f = open(path, 'w', encoding='utf-8')

    line_list = []
    if line_num > 0 :
        for n in range(line_num) :
            line_list.append(str(n+1) + "번째 줄입니다.\n")
        f.writelines(line_list)

    f.close()


def read_all(path):
    f = open(path, 'r', encoding='utf-8')

    line_list = f.readlines()
    for n in line_list :
        print(n, end='')

    return line_list


def append_lines(line_num, path):
    line_list = read_all(path)

    if line_list == 'None' :
        write_lines(line_num, path)

    else :
        f = open(path, 'a', encoding='utf-8')
        append_list = []
        if line_num > 0:
            for n in range(line_num):
                append_list.append(str(n + len(line_list) + 1) + "번째 줄입니다.\n")
            f.writelines(append_list)
            f.close()
