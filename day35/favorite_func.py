from collections import Counter
# 자주 쓰는 함수 만들기

# 1) 리스트의 모든 값이 유니크 (고유하다) 값이면 True 반환하고 아니면 False를 반환하는 함수를 만드시오.
def all_unique(list):
    # 다중 for 문 없이 해결하는 방법을 고안하자 !
    return len(list) == len(set(list))  # True

# set() 함수  set(list)
x = [1, 2, 3, 4, 5]
y = [1, 2, 2, 4, 4]

print(Counter(x))
print(Counter(y))

print(all_unique(x))  #True
print(all_unique(y))  #False

from collections import Counter
# def filter_unique(list):
# ...
# return rtn_list

# 문제1) 리스트에서 고유하지 않은 값을 필터링하세요. return 리스트
# 문제2) 리스트에서 고유한 값을 필터링하세요. return 리스트
# Counter() 클래스 사용 > Counter(list).items()
# (힌트) 리스트 표현식을 사용하세요 list_comprehension !