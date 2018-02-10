import numpy as np

"""
numpay里面有copy和view区别
copy : 在内存里面开辟一个新的块，把原数据完整拷贝到新块
view/reference : 指针的概念，还是指向用来的内存块
"""

# 如果通过简单的赋值操作，那么并没有创建新的内存块和拷贝数据，还是指针的概念
a = np.arange(4)
b = a
c = a
d = b

print("b is a", b is a)
print("c is a", c is a)
print("d is a", d is a)

d[1:3] = [22,33]
print('a\n',a)
print('b\n',b)
print('c\n',c)

# 如果通过copy()函数的赋值操作，那么创建新的内存块，并完整拷贝数据和原矩阵没有关系了
# 不过这样有性能问题，因为创建内存块和拷贝数据都需要资源
a = np.arange(4)
e = a.copy()
print('e\n',e)
e[1:3] = [22,33]
print('a\n',a)
print('e\n',e)