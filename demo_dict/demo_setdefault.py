
'''
setdefault(...)
    当键不存在时，如果没设置值，则返回默认值并更新相应字典
                  如果设置值，则返回值并更新相应字典
    当键存在，则返回键值
    D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
'''
print(help(dict.setdefault))
a = {'one': 1, 'two': 2, 'four': {'five': 5}}
b = a.setdefault('three')
print(b, a)                # None {'two': 2, 'four': {'five': 5}, 'one': 1, 'three': None}
c = a.setdefault('five', 5)
print(c, a)                # 5 {'two': 2, 'four': {'five': 5}, 'five': 5, 'one': 1, 'three': None}
d = a.setdefault('one', 1)
print(d, a)                # 1 {'two': 2, 'four': {'five': 5}, 'five': 5, 'one': 1, 'three': None}