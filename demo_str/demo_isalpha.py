
'''
isalpha(...)
    检测字符串是否只由字母组成
    S.isalpha() -> bool

    Return True if all characters in S are alphabetic
    and there is at least one character in S, False otherwise.
None
'''
print(help(str.isalpha))
a = "thisisstringexamplewow"
b = "123"
c = 'asdf1234'
d = 'asdf!@@#'
e = 'a = "this is string example wow"'
print(a.isalpha())                  # True   全部由字母构成
print(b.isalpha())                  # False  有数字
print(c.isalpha())                  # False  有数字
print(d.isalpha())                  # False  没有字母
print(e.isalpha())                  # False  有空格
