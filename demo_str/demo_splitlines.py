
'''
splitlines(...)
    按照行分隔，返回一个包含各行作为元素的列表，如果 num 指定则仅切片 num 个行
    S.splitlines([keepends]) -> list of strings

    Return a list of the lines in S, breaking at line boundaries.
    Line breaks are not included in the resulting list unless keepends
    is given and true.
'''
print(help(str.splitlines))
a = '11\n22\n33\n44\n55'
print(a.splitlines())                      # ['11', '22', '33', '44', '55']
print(a.splitlines(1))                     # ['11\n', '22\n', '33\n', '44\n', '55']
print(a.splitlines(2))                     # ['11\n', '22\n', '33\n', '44\n', '55']