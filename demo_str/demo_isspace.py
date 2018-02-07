
'''
isspace(...)
    S.isspace() -> bool
    判断字符串是否仅包含空格或制表符。注意：空格字符与空白是不同的
    Return True if all characters in S are whitespace
    and there is at least one character in S, False otherwise.
'''
print(help(str.isspace))
a = ""
c = 'Ssdf1234\t'
d = ' '
e = '\t'
print(a.isspace())                  # False   空白不算空格字符
print(c.isspace())                  # False   不仅仅只有制表符，还有其他字符
print(d.isspace())                  # True    空格字符
print(e.isspace())                  # True    制表符