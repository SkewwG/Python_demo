
'''
copy(...)
    # 浅拷贝， 只是copy了列表里元素的地址，如果是嵌套的，则得用深拷贝
    L.copy() -> list -- a shallow copy of L
'''
print(help(list.copy))
a = [1, 2, 3, 4, [5, 6]]
b = a.copy()
print(a, b)                            # [1, 2, 3, 4, [5, 6]] [1, 2, 3, 4, [5, 6]]
a[1] = 8
print(a, b)                            # [1, 8, 3, 4, [5, 6]] [1, 2, 3, 4, [5, 6]]
a[4][0] = 7
print(a, b)                            # [1, 2, 3, 4, [7, 6]] [1, 2, 3, 4, [7, 6]]
# 原来主列表只是存储了嵌套列表在内存中的地址，而不是所看到的数据，
# copy的也只是嵌套列表的地址，但两个地址指向的是内存中同一块区域，
# 所以在对嵌套列表进行修改时，只是通过了两个复制地址而修改了真实数据，所以两个列表的元素都被改掉了。


import copy
'''
deepcopy(x, memo=None, _nil=[])
    # 深拷贝
    Deep copy operation on arbitrary Python objects.
    
    See the module's __doc__ string for more info.
'''
print(help(copy.deepcopy))
c = [1, 2, 3, 4, [5, 6]]
d = copy.deepcopy(c)
print(c, d)                            # [1, 2, 3, 4, [5, 6]] [1, 2, 3, 4, [5, 6]]
c[1] = 8
print(c, d)                            # [1, 8, 3, 4, [5, 6]] [1, 2, 3, 4, [5, 6]]
c[4][0] = 7
print(c, d)                            # [1, 8, 3, 4, [7, 6]] [1, 2, 3, 4, [5, 6]]