
'''
reverse(...)
    list.reverse()==list[::-1]： 反向列表中元素
    L.reverse() -- reverse *IN PLACE*
'''
print(help(list.reverse))
a = [1, 3, 2, 3, 3, 4, [5, 6], 'a', 'b', 'a', 'a', 'a']
a.reverse()
print(a)            # ['a', 'a', 'a', 'b', 'a', [5, 6], 4, 3, 3, 2, 3, 1]
