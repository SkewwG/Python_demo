
'''
split(...)
    通过指定分隔符对字符串进行切片，如果参数num有指定值，则仅分隔 num 个子字符串
    S.split(sep=None, maxsplit=-1) -> list of strings

    Return a list of the words in S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are
    removed from the result.
'''
print(help(str.split))
a = "abcdeabcdeabcdeabcdeabcdeabcde"
print(a.split('c'))                        # ['ab', 'deab', 'deab', 'deab', 'deab', 'deab', 'de']
print(a.split('c', 1))                     # ['ab', 'deabcdeabcdeabcdeabcdeabcde']
print(a.split('c', 3))                     # ['ab', 'deab', 'deab', 'deabcdeabcdeabcde']