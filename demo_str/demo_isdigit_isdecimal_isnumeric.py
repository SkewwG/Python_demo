'''
isdigit()
True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
False: 汉字数字
Error: 无

isdecimal()
True: Unicode数字，，全角数字（双字节）
False: 罗马数字，汉字数字
Error: byte数字（单字节）

isnumeric()
True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
False: 无
Error: byte数字（单字节）
'''
num = "1"  #unicode
a = num.isdigit()   # True
b = num.isdecimal() # True
c = num.isnumeric() # True
print(a, b, c)

num = "1" # 全角
d = num.isdigit()   # True
e = num.isdecimal() # True
f = num.isnumeric() # True
print(d, e, f)

# num = b"1" # byte
# g = num.isdigit()   # True
# h = num.isdecimal() # AttributeError 'bytes' object has no attribute 'isdecimal'
# i = num.isnumeric() # AttributeError 'bytes' object has no attribute 'isnumeric'
# print(g, h, i)

num = "IV" # 罗马数字
j = num.isdigit()   # True
k = num.isdecimal() # False
l = num.isnumeric() # True
print(j, k, l)

num = "四" # 汉字
m = num.isdigit()   # False
n = num.isdecimal() # False
o = num.isnumeric() # True
print(m, n, o)