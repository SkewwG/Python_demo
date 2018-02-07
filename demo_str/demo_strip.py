
'''
strip(...)
    用于移除字符串头尾指定的字符（默认为空格）
    S.strip([chars]) -> str

    Return a copy of the string S with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in chars instead.
'''
print(help(str.strip))
a = '   asdfzxcvqwer   '
b = '***asdfzxcvqwer***'
print(a.strip())                        # asdfzxcvqwer
print(b.strip('*'))                     # asdfzxcvqwer


