
'''
remove(...)
    list.remove(obj)：      移除列表中某个值的第一个匹配项
    L.remove(value) -> None -- remove first occurrence of value.
    Raises ValueError if the value is not present.
'''
print(help(list.remove))
a = [1, 3, 2, 3, 3, 4, [5, 6], 'a', 'b', 'a', 'a', 'a']
a.remove(3)
a.remove('a')
print(a)            # [1, 2, 3, 3, 4, [5, 6], 'b', 'a', 'a', 'a']
