# <map expression> for <name> in <sequence expression> if <filter expression>

a = (x * 2 for x in range(10) if x % 2 == 0)
print(a)            # <generator object <genexpr> at 0x0000000002A69E10>
b = list((x * 2 for x in range(10) if x % 2 == 0))
print(b)            # [0, 4, 8, 12, 16]

def double(x):
    return x * 2

c = list((double(x) for x in range(10) if x % 2 == 0))
print(c)            # [0, 4, 8, 12, 16]

d = list(lambda x : x * 2 for x in range(10) if x % 2 == 0)
print(d)            # 错误

e = lambda x : x * 2
f = list(d for x in range(10) if x % 2 == 0)

# 总结：使用生成器表达式，要先把函数定义出来！