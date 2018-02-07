# 判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
# 可选参数"start"与"end"为检索字符串的开始与结束位置。

'''
endswith(...)
    S.endswith(suffix[, start[, end]]) -> bool

    suffix -- 该参数可以是一个字符串或者是一个元素。
    start -- 字符串中的开始位置。
    end -- 字符中结束位置。

    Return True if S ends with the specified suffix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    suffix can also be a tuple of strings to try.
'''
print(help(str.endswith))
a = 'asdfsghjk'
b = a.endswith('k')
c = a.endswith('j')
d = a.endswith('a', 0, 1)
e = a.endswith('a', 0, 2)
print(b)                             # b = True
print(c)                             # c = False
print(d)                             # d = True
print(e)                             # e = False