
'''
isupper(...)
    检测字符串中所有的字母是否都为大写
    S.isupper() -> bool

    Return True if all cased characters in S are uppercase and there is
    at least one cased character in S, False otherwise.
'''
print(help(str.isupper))
a = "Thisisstringexamplewow"
b = "ThisisstRingexamplewow"
c = 'ASD'
print(a.isupper())                  # False   有小写字符
print(b.isupper())                  # False   有小写字符
print(c.isupper())                  # True    全部大写