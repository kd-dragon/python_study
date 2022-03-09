from collections import Counter

y = [1, 2, 2, 3, 3, 4, 4, 5, ]

def filter_not_unique(list):
    not_unique_list = [key for key,value in Counter(list).items() if value != 1]
    return not_unique_list

print(filter_not_unique(y))

def filter_unique(list):
    unique_list = [key for key,value in Counter(list).items() if value == 1]
    return unique_list

print(filter_unique(y))

