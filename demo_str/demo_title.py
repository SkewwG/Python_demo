
'''
title(...)
    返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写
    S.title() -> str

    Return a titlecased version of S, i.e. words start with title case
    characters, all remaining cased characters have lower case.
'''
print(help(str.title))
a = 'asdfzxcvqwer'
b = 'ASDFQWERZXCV'
c = 'asdfQWER'
print(a.title())                         # Asdfzxcvqwer
print(b.title())                         # Asdfqwerzxcv
print(c.title())                         # Asdfqwer

