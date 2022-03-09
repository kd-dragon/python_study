import numpy as np

data = [[1, 2, 3]
      , [4, 5, 6]
      , [7, 8, 9]
    ]

# 행렬 원소의 연산 !!!

ndata = np.arange(1, 10).reshape(3, 3)

# ==========================================================

# 행렬의 연산
# 차원 !

# 0 차원 행렬
a = np.array(1)
print(a)
print(a.shape)
print(str(a.ndim) + "차원")
print("====================================")

# 1 차원 행렬  ( 벡터!!!  ) 벡터 = 1차원 행렬이다!
b = np.array([3, 6, 9])
print(b)
print(b.shape)
print(str(b.ndim) + "차원")
print("====================================")
c = np.array([[1,2],[3,4]])
print(c)
print(c.shape)
print(str(c.ndim) + "차원")

print("====================================")

# 3차원 행렬 이상은 Tensor 라고 부른다!
d = np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]])
print(d)
print(d.shape)
print(str(d.ndim) + "차원")

# TensorFlow ??

# 텐서플로우는 다차원 배열을 가지고 뭔가 연산을해서 결과를 도출해낸다!
