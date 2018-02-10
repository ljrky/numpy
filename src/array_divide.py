import numpy as np

"""
等量分割：
np.split对矩阵进行分割，不过分割出来的不是矩阵，而是一个list，需要访问list的element才是矩阵
参数如下：
1，ary=A
2，indices_or_sections=2 ：分成2块
3，axis=1 ：横向分割 np.hsplit()函数效果一样
3，axis=0 ：纵向分割 np.vsplit()函数效果一样

"""

A = np.arange(12).reshape((3, 4))
print('A\n', A)

print("等量分割")
# 横向分割，注意判断列数能不能被indices_or_sections参数整除
B = np.split(ary=A, indices_or_sections=2, axis=1)
print('B\n', B)
B_hsplit = np.hsplit(A,2)
print("B_hsplit\n", B_hsplit)



# 纵向分割，注意判断行数能不能被indices_or_sections参数整除
C = np.split(ary=A, indices_or_sections=3, axis=0)
print('C\n', C)
print('C shape\n', C[0].shape)
C_vsplit = np.vsplit(A,3)
print('C_vsplit\n', C_vsplit)


"""
不等量分割：
np.array_split对矩阵进行分割，不过分割出来的不是矩阵，而是一个list，需要访问list的element才是矩阵
参数如下：
1，ary=A
2，indices_or_sections=2 ：分成2块
3，axis=1 ：横向分割
"""

print("不等量分割")
A = np.arange(12).reshape((3, 4))
print('A\n', A)

# 横向分割
B = np.array_split(ary=A, indices_or_sections=3, axis=1)
print('B\n', B)

# 纵向分割
C = np.array_split(ary=A, indices_or_sections=2, axis=0)
print('C\n', C)
print('C shape\n', C[0].shape)