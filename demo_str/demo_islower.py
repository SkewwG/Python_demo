
'''
islower(...)
    检测字符串是否由小写字母组成
    S.islower() -> bool

    Return True if all cased characters in S are lowercase and there is
    at least one cased character in S, False otherwise.

None
'''
print(help(str.islower))
a = "Thisisstringexamplewow"
c = 'Ssdf1234'
d = 'asdf!@@#'
e = 'a = "this is string example wow"'
print(a.islower())                  # False   有大写字母
print(c.islower())                  # False   有大写字母
print(d.islower())                  # True    全部小写
print(e.islower())                  # True    全部小写
