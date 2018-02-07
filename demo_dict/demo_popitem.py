
'''
popitem(...)
    移除随机的项
    D.popitem() -> (k, v), remove and return some (key, value) pair as a
    2-tuple; but raise KeyError if D is empty.
'''
print(help(dict.popitem))
a = {'one': 1, 'two': 2, 'four': {'five': 5}}
b = a.popitem()
print(b, a)                # ('four', {'five': 5}) {'one': 1, 'two': 2}或者('one', 1) {'two': 2, 'four': {'five': 5}}