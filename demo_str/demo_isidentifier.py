
'''
isidentifier(...)
    判断字符串是否是合法的标识符，字符串仅包含中文字符合法，实际上这里判断的是变量名是否合法
    S.isidentifier() -> bool

    Return True if S is a valid identifier according
    to the language definition.

    Use keyword.iskeyword() to test for reserved identifiers
    such as "def" and "class".
'''
print(help(str.isidentifier))
a = "thisisstringexamplewow"
b = "123"
c = 'asdf1234'
d = 'asdf!@@#'
e = 'a = "this is string example wow"'
print(a.isidentifier())                  # True   全部由字母构成
print(b.isidentifier())                  # False  不能以数字开头
print(c.isidentifier())                  # True   字母开头合法
print(d.isidentifier())                  # False  有特殊字符（不能有除了字母数字下划线的其他字符）
print(e.isidentifier())                  # False  有空格（不能有除了字母数字下划线的其他字符）
