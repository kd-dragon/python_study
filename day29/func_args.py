def sum(default, *nodes):
    print(f"args={nodes}, type={type(nodes)}")
    cnt = default
    for x in nodes:
        cnt += x
    return cnt

print(sum(100, 1,2,3,4,5,6,7,8,9))


# *args     #tuple (리스트와 비슷한데 데이터 변경이 불가능) immutable!
# **kwargs  #dictionary (key, value)

