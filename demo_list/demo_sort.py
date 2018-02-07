
'''
sort(...)
    list.sort([func])：          对原列表进行排序    reverse==True时，按降序排列
    L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
'''
print(help(list.sort))
a = [6, 1, 5, 9, 3, 7]
a.sort()
print(a)            # [1, 3, 5, 6, 7, 9]
a.sort(reverse=True)
print(a)            # [9, 7, 6, 5, 3, 1]