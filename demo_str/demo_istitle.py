
'''
istitle(...)
    检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
    S.istitle() -> bool

    Return True if S is a titlecased string and there is at least one
    character in S, i.e. upper- and titlecase characters may only
    follow uncased characters and lowercase characters only cased ones.
    Return False otherwise.
'''
print(help(str.istitle))
a = "Thisisstringexamplewow"
b = "ThisisstRingexamplewow"
c = 'ssdf1234'
print(a.istitle())                  # True   首字符大写，其他字符全小写
print(b.istitle())                  # False  首字符大写，其他字符并不是全小写
print(c.istitle())                  # False  首字符不是大写