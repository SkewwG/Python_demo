
'''
isalnum(...)
    检测字符串是否由字母或数字组成
    S.isalnum() -> bool

    Return True if all characters in S are alphanumeric
    and there is at least one character in S, False otherwise.

None
'''
print(help(str.isalnum))
a = "thisisstringexamplewow"
b = "123"
c = 'asdf1234'
d = 'asdf!@@#'
e = 'a = "this is string example wow"'
print(a.isalnum())                  # True  全部由字母构成
print(b.isalnum())                  # True  全部由数字构成
print(c.isalnum())                  # True  全部由字母或者数字构成
print(d.isalnum())                  # False 有特殊字符
print(e.isalnum())                  # False 有空格
