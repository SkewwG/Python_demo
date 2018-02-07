
'''
pop(...)
    list.pop()：            移除列表中的最后一个元素，并且返回该元素的值
    list.pop(index)：       移除列表中下表为index的元素，并且返回该元素的值
    L.pop([index]) -> item -- remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.
'''
print(help(list.pop))
a = [1, 3, 2, 3, 3, 4, [5, 6], 'a', 'a', 'a', 'a']
b = a.pop()
c = a.pop(2)
print(a)            # [1, 3, 3, 3, 4, [5, 6], 'a', 'a', 'a']
print(b)            # a
print(c)            # 2
