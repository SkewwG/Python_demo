
'''
values(...)
    D.values() -> an object providing a view on D's values
'''
print(help(dict.values))
a = {'one': 1, 'two': 2, 'four': {'five': 5}}
b = a.values()
print(b)                # dict_values([1, {'five': 5}, 2])
print(list(b))          # [1, {'five': 5}, 2]
