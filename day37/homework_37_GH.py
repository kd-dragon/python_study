from collections import Counter

list = [1, 2, 2, 3, 3, 4, 4, 5, ]


def filter_unique(list):
    return [i for i, j in Counter(list).items() if j == 1]


def filter_common(list):
    return [i for i, j in Counter(list).items() if j > 1]


print(filter_unique(list))
print(filter_common(list))