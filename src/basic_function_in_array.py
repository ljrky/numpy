import numpy as np

"""
获取矩阵中最大，最小值的索引
求平均值和中位数
求累加函数
矩阵行排序
通过索引访问矩阵的值
矩阵转置
"""

a = np.arange(0,20).reshape((4,5))
# 获得矩阵中最大或者最小值的索引
print(a)
print("max item", np.argmax(a))
print("min item", np.argmin(a))

# 获得矩阵的平均值
print("mean", np.mean(a))
print("average", np.average(a))
# 获得矩阵的中位数
print("median", np.median(a))
# 获得累加矩阵
print("cumsum", np.cumsum(a))
# 矩阵行排序
b = np.random.random((3,3))
print("b",b)
print(np.sort(b))

# 通过索引访问矩阵的值
# x为行数，索引/列数
# y为列数，索引%列数
x = int(np.argmax(a) / 5)
y = np.argmax(a) % 5
print(x,y,a[x,y])

# 矩阵转置
a = np.arange(0,10,1).reshape(2,5)
print(a)
print(a.shape)
b = a.T
print(b)
print(b.shape)