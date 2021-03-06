import numpy as np

a = np.arange(10)
b = np.arange(9).reshape(3, 3)  # 3 X 4 행렬 배열로 Reshape
print("=====================")
# 브로드 캐스팅 연산


# 슬라이싱
# 인덱스 자리에 콜론(:) 을 이용해서 범위를 지정하면 슬라이싱된다..
# 이때 범위의 끝 인덱스는 슬라이싱 결과에 포함 X a <= 원소 < b
# 시작과 끝 인덱스를 각각 생략하면 처음부터 끝까지라는 의미다.
print(b)
print("====================")
print(b[0:2, 1:3])

