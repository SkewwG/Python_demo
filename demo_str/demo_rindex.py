
'''
rindex(...)
    返回子字符串 str 在字符串中最后出现的位置，
    如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间
    S.rindex(sub[, start[, end]]) -> int

    Like S.rfind() but raise ValueError when the substring is not found.
'''
print(help(str.rindex))
a = "ASDfgh*123456ASDfgh*123456ASDfgh*123456ASDfgh*123456"
print(a.rindex('*'))                     # 45
print(a.rindex('*', 0, 7))               # 6
print(a.rindex('*', 0, 6))               # 报错