import numpy as np

"""
使用take函数获取索引的值
通过索引访问矩阵的值，类似数组访问，不过区别是：
如果只提供行的索引，会返回整行
如果想要获得列可以先转置，然后提供行的索引
"""

a = np.arange(0, 20).reshape((4, 5))

# 只提供行
print(a)
print(a[3])
print(a[1, 4])
print(a.T[1])

# 通过索引访问矩阵的值
# x为行数，索引/列数
# y为列数，索引%列数
# 或者使用take(矩阵，索引)函数访问
print(a)
x = int(np.argmax(a) / 5)
y = np.argmax(a) % 5
print(x, y, a[x, y])
print(np.argmin(a), np.take(a, np.argmin(a)))
