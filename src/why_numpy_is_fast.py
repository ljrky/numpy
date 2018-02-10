import numpy as np
import time
import pandas as pd


def time_consumes():
    global t0, t1, t2
    t0 = time.time()
    f1(a)
    t1 = time.time()
    f2(b)
    t2 = time.time()
    print('%f' % ((t1 - t0) / N))
    print('%f' % ((t2 - t1) / N))


""""
在不同的内存存储模式下，性能区别
如果行式存储，C-type,对以行为单位的聚合操作比较快
如果列式存储，F-type,对以列为单位的聚合操作比较快
"""
a = np.zeros((200, 200), order="C")
b = np.zeros((200, 200), order="F")
N = 9999


def f1(a):
    for _ in range(N):
        np.concatenate((a, a), axis=1)


def f2(a):
    for _ in range(N):
        np.concatenate((b, b), axis=1)


print("C-type and Fortun type diff")
time_consumes()

"""
Copy和View的比较
Copy是把数据拷贝另外一块内存去，速度慢，例子：
1，b = b * 2 : 因为创建了一个copy
2，ravel() ：因为创建了一个copy，并返回copy
View只是指针，不做数据拷贝，速度快，例子：
1，a *= 2
2，flatten() ：因为只返回了一个view
"""

a = np.arange(1, 7).reshape((3, 2))
a_view = a[:2]
a_copy = a[:2].copy()

a_copy[1, 1] = 0
print(a)

a_view[1, 1] = 0
print(a)

# 性能测试
a = np.zeros((1000, 1000))
b = np.zeros((1000, 1000))
N = 999


def f1(a):
    for _ in range(N):
        a *= 2


def f2(b):
    for _ in range(N):
        b = b * 2


print("view and copy diff")
time_consumes()

"""
如何用numpy实现panda的类似数据库表的功能，以提高速度
"""
a = np.zeros(3, dtype=[('foo', np.int32), ('bar', np.float16)])
b = pd.DataFrame(np.zeros((3, 2), dtype=np.int32), columns=['foo', 'bar'])


def f1(a):
    for _ in range(N):
        a['bar'] *= a['foo']


def f2(b):
    for _ in range(N):
        b['bar'] *= b['foo']


print("numpy and pandas diff")
time_consumes()
