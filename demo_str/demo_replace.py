
'''
replace(...)
    把字符串中的 old（旧字符串）替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
    S.replace(old, new[, count]) -> str

    Return a copy of S with all occurrences of substring
    old replaced by new.  If the optional argument count is
    given, only the first count occurrences are replaced.
'''
print(help(str.replace))
a = "ASDfgh*123456ASDfgh*123456ASDfgh*123456ASDfgh*123456"
print(a.replace('*', '-'))                  # ASDfgh-123456ASDfgh-123456ASDfgh-123456ASDfgh-123456
print(a.replace('*', '-', 2))               # ASDfgh-123456ASDfgh-123456ASDfgh*123456ASDfgh*123456