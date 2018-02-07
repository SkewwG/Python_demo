
'''
partition(...)
    根据指定的分隔符将字符串进行分割
    （返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串）
    S.partition(sep) -> (head, sep, tail)

    Search for the separator sep in S, and return the part before it,
    the separator itself, and the part after it.  If the separator is not
    found, return S and two empty strings.
'''
print(help(str.partition))
a = "ASDfgh*123456"
print(a.partition('*'))                  # ('ASDfgh', '*', '123456')