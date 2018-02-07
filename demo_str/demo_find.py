
'''
find(...)
    检测字符串中是否包含子字符串 str ，
    如果指定 beg（开始）和 end（结束）范围，则检查是否包含在指定范围内，
    如果包含子字符串，则返回开始的索引值，否则返回-1。

    S.find(sub[, start[, end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.
'''
print(help(str.find))
a = 'asdfsghjk'
b = a.find('d')
c = a.find('f', 1, 4)               #
d = a.find('f', 1, 3)
print(b)                            # 2 下标
print(c)                            # 2 从第一个字符到第三个字符中找，找到了则返回下标
print(d)                            # -1
