
'''
pop(...)
    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    If key is not found, d is returned if given, otherwise KeyError is raised
'''
print(help(dict.pop))
a = {'one': 1, 'two': 2, 'four': {'five': 5}}
b = a.pop('one')
print(b, a)                # 1 {'two': 2, 'four': {'five': 5}}