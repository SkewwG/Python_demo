
'''
lstrip(...)
    用于截掉字符串左边的空格或指定字符
    S.lstrip([chars]) -> str

    Return a copy of the string S with leading whitespace removed.
    If chars is given and not None, remove characters in chars instead.
'''
print(help(str.lstrip))
a = "***ASDfgh"
b = '***ASDfgh'
c = '   asdfsadf'
print(a.lstrip())                  # ***ASDfgh
print(b.lstrip('*'))               # ASDfgh
print(c.lstrip())                  # asdfsadf