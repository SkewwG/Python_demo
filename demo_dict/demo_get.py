
'''
get(...)
    如果键k存在，则返回键K的值，如果不存在则返回None
    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
'''
print(help(dict.get))
a = {'one': 1, 'two': 2, 'four': {'five': 5}}
b = a.get('one')
c = a.get('three')
print(b)                # 1
print(c)                # None