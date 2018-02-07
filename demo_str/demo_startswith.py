
'''
startswith(...)
    用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。
    如果参数 beg 和 end指定值，则在指定范围内检查
    S.startswith(prefix[, start[, end]]) -> bool

    Return True if S starts with the specified prefix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    prefix can also be a tuple of strings to try.
'''
print(help(str.startswith))
a = 'asdfzxcvqwer'
print(a.startswith('a'))                         # True
print(a.startswith('s',1,2))                     # True
print(a.startswith('s',2,3))                     # False