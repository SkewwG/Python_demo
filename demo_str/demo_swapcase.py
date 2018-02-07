
'''
swapcase(...)
    用于对字符串的大小写字母进行转换(小写转大写，大写转小写)
    S.swapcase() -> str

    Return a copy of S with uppercase characters converted to lowercase
    and vice versa.
'''
print(help(str.swapcase))
a = 'asdfzxcvqwer'
b = 'ASDFQWERZXCV'
c = 'asdfQWER'
print(a.swapcase())                         # ASDFZXCVQWER
print(b.swapcase())                         # asdfqwerzxcv
print(c.swapcase())                         # ASDFqwer

