import numpy as np

"""
几种 array 的属性:

ndim：维度
shape：行数和列数
size：元素个数
"""

# 列表转为矩阵
array = np.array([[1,2,3],[2,3,4]])
print(array)

# 矩阵的维度
print("number of dim:", array.ndim)

# 矩阵的行数和列数
print("shape:", array.shape)

# 矩阵的元素个数
print("size", array.size)