
'''
ljust(...)
    返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。
    如果指定的长度小于原字符串的长度则返回原字符串。
    S.ljust(width[, fillchar]) -> str

    Return S left-justified in a Unicode string of length width. Padding is
    done using the specified fill character (default is a space).
'''
print(help(str.ljust))
a = "asdf"
print(a.ljust(8))                  # asdf
print(a.ljust(8, '+'))             # asdf++++