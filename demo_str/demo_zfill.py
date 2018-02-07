
'''
zfill(...)
    返回一个长度为width的数字字符串，最左边填充0。
    如果width小于等于原字符串长度，则返回原字符串。主要用于数字类字符串的格式化
    S.zfill(width) -> str

    Pad a numeric string S with zeros on the left, to fill a field
    of the specified width. The string S is never truncated.
'''
print(help(str.zfill))
a = '123456'
print(a.zfill(10))                         # 0000123456

