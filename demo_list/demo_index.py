
'''
index(...)
    从列表中找出某个值第一个匹配项的索引位置
    L.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.
'''
print(help(list.index))
a = [1, 3, 2, 3, 3, 4, [5, 6], 'a', 'a', 'a', 'a']
b = a.index(3)
c = a.index('a')
print(b)            # 1
print(c)            # 7
