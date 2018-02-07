
'''
rfind(...)
    返回字符串最后一次出现的位置，如果没有匹配项则返回-1
    S.rfind(sub[, start[, end]]) -> int

    Return the highest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.
'''
print(help(str.rfind))
a = "ASDfgh*123456ASDfgh*123456ASDfgh*123456ASDfgh*123456"
print(a.rfind('*'))                     # 45
print(a.rfind('*', 0, 7))               # 6
print(a.rfind('*', 0, 6))               # -1