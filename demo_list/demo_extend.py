
'''
extend(...)
    将参数作为一个列表去扩展列表的末尾
    L.extend(iterable) -> None -- extend list by appending elements from the iterable
'''
print(help(list.extend))
a = [1, 2, 3, 4]
a.extend([5,6])
print(a)                            # [1, 2, 3, 4, 5, 6]
