
'''
append(...)
    将参数作为一个元素添加到列表的末尾
    L.append(object) -> None -- append object to end
'''
print(help(list.append))
a = [1, 2, 3, 4]
a.append([5,6])
print(a)                            # [1, 2, 3, 4, [5, 6]]
