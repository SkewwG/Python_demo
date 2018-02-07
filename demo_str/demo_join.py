
'''
join(...)
    用于将序列中的元素以指定的字符连接生成一个新的字符串。
    S.join(iterable) -> str

    Return a string which is the concatenation of the strings in the
    iterable.  The separator between elements is S.
'''
print(help(str.join))
a = "Thisisstringexamplewow"
b = "-"
c = b.join(a)
print(c)                  # T-h-i-s-i-s-s-t-r-i-n-g-e-x-a-m-p-l-e-w-o-w
z = 'aaa'
x = ['b','b','b']
c = '&'.join([z, x[1:]])
print(c)