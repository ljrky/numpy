import numpy as np
"""
1，给一个数组创建矩阵
2，创建全为0的矩阵
3，创建全为1的矩阵
4，创建随机数的矩阵
5，把多维矩阵展开成一维矩阵
"""

# 创建一维矩阵
a = np.array([2,3,4])
print(a.ndim)
print(a.shape)

# 指定矩阵的数据类型
b = np.array([2,3,4],dtype=np.int32)
c = np.array([2,3,4],dtype=np.float32)

print(a.dtype)
print(b.dtype)
print(c.dtype)

# 创建二维矩阵,2行-3列
d = np.array([[2,23,4],[2,32,4]])
print(d)
print(d.ndim)
print(d.shape)
# 重构矩阵
d_resharp = d.reshape((3,2))
print("d resharped")
print(d_resharp)
print(d_resharp.shape)

# 创建2维全为0的矩阵，3行-4列
e = np.zeros((3,4))
print(e)
print(e.ndim)
print(e.shape)


# 创建全为1的数组，3行-4列
f = np.ones((3,4))
print(f)

# 创建随机数字填充的矩阵
g = np.random.random((2,4))
print("random generated vector")
print(g)

# 根据范围和步数创建矩阵
h = np.arange(10, 20, 2)
print(h)

# 使用reshape重构矩阵,reshape函数返回一个新的矩阵
i = np.arange(0,12).reshape((3,4))
print(i)

# 使用linspace生成给定范围内根据给定个数平均的矩阵
j = np.linspace(1,10,10)
print(j)
print(j.size)
k = j.reshape((2,5))
print(k)
print(k.shape)


# 多维矩阵展开为一维矩阵
l = np.arange(0,50).reshape((5,10))
print(l)
m = l.flatten()
print(m)