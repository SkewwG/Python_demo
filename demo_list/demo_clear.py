
'''
clear(...)
    列表仍然存在，只是成了空列表
    L.clear() -> None -- remove all items from L
'''
print(help(list.clear))
a = [1, 2, 3, 4]
a.clear()
print(a)                            # []
