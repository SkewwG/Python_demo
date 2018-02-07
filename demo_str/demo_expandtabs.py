# 判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
# 可选参数"start"与"end"为检索字符串的开始与结束位置。

'''
expandtabs(...)
    S.expandtabs(tabsize=8) -> str

    Return a copy of S where all tab characters are expanded using spaces.
    If tabsize is not given, a tab size of 8 characters is assumed.
'''
print(help(str.expandtabs))
a = 'asdfsghjk'
b = a.endswith('k')
c = a.endswith('j')
d = a.endswith('a', 0, 1)
e = a.endswith('a', 0, 2)
print(b)                             # b = True
print(c)                             # c = False
print(d)                             # d = True
print(e)                             # e = False