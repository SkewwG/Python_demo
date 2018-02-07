
'''
index(...)
    检测字符串string中是否包含子字符串 str ，
    如果存在，则返回str在string中的索引值，
    如果指定beg（开始）和 end（结束）范围，则检查是否包含在指定范围内，
    该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常(ValueError: substring not found)。
    S.index(sub[, start[, end]]) -> int

    Like S.find() but raise ValueError when the substring is not found.

None
'''
print(help(str.index))
a = "this is string example....wow!!!"
b = "exam"
c = a.index(b)
d = a.index(b, 20)
print(c)                            # 15  返回b字符串的第一个字符的索引值
print(d)                            # 报错
