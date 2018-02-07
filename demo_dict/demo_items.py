
'''
items(...)
    将所有的字典项以列表方式返回，这些列表项中的每一项都来自于(键，值)
    D.items() -> a set-like object providing a view on D's items
'''
print(help(dict.items))
a = {'one': 1, 'two': 2, 'four': {'five': 5}}
b = a.items()
print(b)                # dict_items([('two', 2), ('four', {'five': 5}), ('one', 1)])
print(list(b))          # [('two', 2), ('four', {'five': 5}), ('one', 1)]
