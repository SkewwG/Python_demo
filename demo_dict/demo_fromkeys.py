
'''
fromkeys(iterable, value=None, /) method of builtins.type instance
    使用给定的键建立新的字典，每个键默认的对应的值为none
    不要用他修改原有的字典，不然会覆盖掉
    Returns a new dict with keys from iterable and values equal to value.
'''
print(help(dict.fromkeys))
a = {}.fromkeys(['three'])
b = {}.fromkeys(['one', 'two'], 1)
c = {}.fromkeys(['one', 'two'], [1, 2])
print(a)                # {'three': None}
print(b)                # {'two': 1, 'one': 1}
print(c)                # {'two': [1, 2], 'one': [1, 2]}