
'''
count(...)
    list.count(obj)：       统计某个元素在列表中出现的次数
    L.count(value) -> integer -- return number of occurrences of value
'''
print(help(list.count))
a = [1, 3, 2, 3, 3, 4, [5, 6], 'a', 'a', 'a', 'a']
b = a.count('a')
print(b)                                # 4
c = a.count(3)
print(c)                                # 3