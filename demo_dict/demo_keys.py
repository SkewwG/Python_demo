
'''
keys(...)
    D.keys() -> a set-like object providing a view on D's keys
'''
print(help(dict.keys))
a = {'one': 1, 'two': 2, 'four': {'five': 5}}
b = a.keys()
print(b)                # dict_keys(['four', 'one', 'two'])
print(list(b))          # ['four', 'one', 'two']
