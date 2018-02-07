
'''
clear(...)
    字典仍然存在，只是成了空字典
    D.clear() -> None.  Remove all items from D.
'''
print(help(dict.clear))
a = {'one':1,'two':2,'three':3}
a.clear()
print(a)            # {}
