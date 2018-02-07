
'''
update(...)
    利用一个字典项更新另外一个字典
    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]
'''
print(help(dict.update))
a = {'one': 1, 'two': 2, 'four': {'five': 5}}
b = {'one': 3}                  # for k in E: D[k] = E[k]
c = {'one': 4, 'three': 3}      # for k, v in E: D[k] = v
d = {'three': 3}                # for k in F:  D[k] = F[k]
a.update(b)
print(a)                # {'one': 3, 'four': {'five': 5}, 'two': 2}
a.update(c)
print(a)                # {'one': 4, 'four': {'five': 5}, 'two': 2, 'three': 3}
a.update(d)
print(a)                # {'one': 4, 'four': {'five': 5}, 'two': 2, 'three': 3}