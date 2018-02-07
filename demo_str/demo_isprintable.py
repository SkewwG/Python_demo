
'''
isprintable(...)
    判断字符串所包含的字符是否全部可打印。字符串包含不可打印字符，如转义字符，将返回False。
    S.isprintable() -> bool

    Return True if all characters in S are considered
    printable in repr() or S is empty, False otherwise.
'''
print(help(str.isprintable))
a = "Thisisstringexamplewow"
c = 'Ssdf1234\t'
d = 'asdf!@@#\n'
e = 'a = "this is string example wow"\a'
print(a.isprintable())                  # True
print(c.isprintable())                  # False   有制表符
print(d.isprintable())                  # False   有换行符
print(e.isprintable())                  # False
