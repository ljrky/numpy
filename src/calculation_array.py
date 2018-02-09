import numpy as np

"""
一维矩阵计算
"""
a = np.arange(10, 41, 10)
b = np.arange(4)

print(a)
print(b)

# 矩阵加法 ：对应位置相加

c = a + b
print(c)

# 矩阵减法 ：对应位置相减
d = a - b
print(d)

# 矩阵乘法 : 对应位置相乘
e = a * b
print(e)

# 矩阵平方
f = b ** 2
print(f)

# numpy内置函数工具
g = 10 * np.sin(a)
print(g)
print(g > 0)

"""
多维矩阵计算
"""

"""
Numpy中的矩阵乘法分两种：
1，对应元素相乘的矩阵乘法：用*表示
2，标准的矩阵乘法：用dot方法
"""

"""
标准的矩阵乘法
第一个矩阵第一行的每个数字，各自乘以第二个矩阵第一列对应位置的数字，然后将乘积相加
矩阵乘法前提：第一个矩阵的列数等于第二个矩阵的行数
矩阵乘法结果：行数等于第一个矩阵的行数,列数等于第二个矩阵的列数，公式为(x,y)dot(i,j)=>(x,j)
"""
a = np.array([[1, 1, 1], [0, 1, 0]])
b = np.arange(9).reshape((3, 3))

print(a.shape)
print(b.shape)
c = np.dot(a, b)
print(c)
print(c.shape)

"""
聚合函数
1，max
2，min
3，sum
4，size
5，average
"""

a = np.random.random((2, 4))
print(a)

# 对矩阵中所有的元素进行操作
print("max", np.max(a))
print("min", np.min(a))
print("sum", np.sum(a))
print("count", np.size(a))
print("average", np.average(a))
print("average", np.sum(a) / np.size(a))

"""
对矩阵中的行或者列进行操作
需要使用axis参数
1, axis = 0 : 以列为单元进行聚合
2, axis = 1 : 以行为单位进行聚合
"""

a = np.arange(0, 10, 1).reshape((2, 5))
# 以列为单位进行聚合
print(a)
print("max", np.max(a, axis=0))
print("min", np.min(a, axis=0))
print("sum", np.sum(a, axis=0))
print("count", np.size(a, axis=0))
print("average", np.average(a, axis=0))

# 以行为单位进行聚合
a = np.arange(1, 31, 1).reshape((5, 6))
print(a)
print("max", np.max(a, axis=1))
print("min", np.min(a, axis=1))
print("sum", np.sum(a, axis=1))
print("count", np.size(a, axis=1))
print("average", np.average(a, axis=1))