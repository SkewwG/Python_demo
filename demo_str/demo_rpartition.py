
'''
rpartition(...)
    与str.partition()相反，从原字符串的最右边开始拆分，
    但是同样返回包含三个元素的元组：倒数第一个Sep之前的字符串，Sep字符，Sep之后的字符串。
    注意”倒数Sep之前的字符串”，这个之前的字符串，是从原字符串的最左边开始算，并不是最右边。
    S.rpartition(sep) -> (head, sep, tail)

    Search for the separator sep in S, starting at the end of S, and return
    the part before it, the separator itself, and the part after it.  If the
    separator is not found, return two empty strings and S.
'''
print(help(str.rpartition))
a = "abccdee"
print(a.rpartition('c'))                     # ('abc', 'c', 'dee')
print(a.rpartition('f'))                     # ('', '', 'abccdee')