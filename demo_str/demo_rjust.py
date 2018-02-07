
'''
rjust(...)
    返回的原/新字符串右对齐，且默认使用空格填充至指定长度（width）的新字符串。
    如果指定的长度（width）小于原字符串的长度则返回原字符串
    S.rjust(width[, fillchar]) -> str

    Return S right-justified in a string of length width. Padding is
    done using the specified fill character (default is a space).
'''
print(help(str.rjust))
a = "ASDfgh*123456"
print(a.rjust(20))                     #        ASDfgh*123456
print(a.rjust(20, '-'))                # -------ASDfgh*123456