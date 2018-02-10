import numpy as np

"""
两个矩阵按照行或者列合并
上下合并：vstack : 对两个矩阵上+下合并，前提条件是两个矩阵列数要一样
左右合并：hstack : 对两个矩阵左+右合并，前提条件是两个矩阵行数要一样
一维数组转置成矩阵：newaxis,这样就变成矩阵，可以进行转置等操作
多个矩阵合并：concatenate
"""

a = np.array([[1, 1, 1, 1], [1, 1, 1, 1]])
b = np.array([2, 2, 2, 2])

c = np.vstack((a, b))
print("vertical merge")
print(a.shape, '\n', a)
print(b.shape, '\n', b)
print(c.shape, '\n', c)

a = np.array([[1, 1, 1, 1], [1, 1, 1, 1]])
b = np.array([[2, 2, 2, 2], [2, 2, 2, 2]])
d = np.hstack((a, b))
print("horizontal merge")
print(a.shape, '\n', a)
print(b.shape, '\n', b)
print(d.shape, '\n', d)

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
print('A', '\n', A)
print('A shape ', A.shape)
print('A.T', '\n', A.T)

# np.newaxis在前面，矩阵纵向排列
a = A[np.newaxis, :]
print('a', '\n', a)
print('a shape ', a.shape)
print('a.T', '\n', a.T)

# np.newaxis在后面，矩阵纵向排列
b = B[:, np.newaxis]
print('a', '\n', b)
print('a shape ', b.shape)
print('a.T', '\n', b.T)

"""
1，生成两个数组
2，纵向排列成矩阵
3，上下合并
4，左右合并
5，多个矩阵合并
"""
A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]

C = np.vstack((A, B))  # vertical stack
D = np.hstack((A, B))  # horizontal stack

print("c \n", C)
print("d \n", D)

print("横向合并")
E = np.concatenate((A, B, B, A), axis=1)
print("e \n", E)

print("纵向合并")
F = np.concatenate((A, B, B, A), axis=0)
print("f \n", F)
