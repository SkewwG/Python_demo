
'''
copy(...)
    copy 返回一个具有相同键-值对的新字典(浅拷贝）
    D.copy() -> a shallow copy of D
'''
print(help(dict.copy))
a = {'one': 1, 'two': 2, 'four': {'five': 5}}
b = a.copy()
a['one'] = 4
print(a, b)            # {'four': {'five': 5}, 'one': 4, 'two': 2} {'one': 1, 'four': {'five': 5}, 'two': 2}
a['four']['five'] = 6
print(a, b)            # {'four': {'five': 6}, 'one': 4, 'two': 2} {'one': 1, 'four': {'five': 6}, 'two': 2}
# 当嵌套时全都发生了改变，说明是浅拷贝，拷贝的只是地址，所以嵌套的时候，指向的都是同一个字典
