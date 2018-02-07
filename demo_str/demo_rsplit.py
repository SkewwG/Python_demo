
'''
rsplit(...)
    与str.split()类似，只是它从最右边开始拆分。只有在指定maxsplit的情况下才会看到效果。
    S.rsplit(sep=None, maxsplit=-1) -> list of strings

    Return a list of the words in S, using sep as the
    delimiter string, starting at the end of the string and
    working to the front.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified, any whitespace string
    is a separator.
'''
print(help(str.rsplit))
a = "abcdeabcdeabcdeabcdeabcdeabcde"
print(a.rsplit('c'))                        # 不指定maxsplit，返回的结果与str.split()相同['ab', 'deab', 'deab', 'deab', 'deab', 'deab', 'de']
print(a.rsplit('c', 1))                     # 从右开始拆，只拆一次 ['abcdeabcdeabcdeabcdeabcdeab', 'de']
print(a.rsplit('c', 3))                     # 从右开始拆，拆三次   ['abcdeabcdeabcdeab', 'deab', 'deab', 'de']