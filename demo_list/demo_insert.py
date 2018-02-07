
'''
insert(...)
    list.insert(index,obj)：将元素插入某一位置之前，如果index大于list的长度，最后加。如果index小于0，最开始加
    L.insert(index, object) -- insert object before index
'''
print(help(list.insert))
a = [1, 3, 2, 3, 3, 4, [5, 6], 'a', 'a', 'a', 'a']
a.insert(3, 'b')
print(a)            # [1, 3, 2, 'b', 3, 3, 4, [5, 6], 'a', 'a', 'a', 'a']
