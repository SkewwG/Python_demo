'''
count(...)
    S.count(sub[, start[, end]]) -> int

    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.
'''
print(help(str.count))
a = 'askdfksghjkl'
b = a.count('k')               # 从下标为1到5计数‘s’的个数
print(b)                             # b = 2
