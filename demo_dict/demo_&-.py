# 两个字典中寻找相同点
# 字典的keys()方法和items()方法支持集合操作，比如求并集、交集、差集。而values()方法并不支持集合操作。
a = {
    'x':1,
    'y':2,
    'z':3
}

b = {
    'w':10,
    'x':11,
    'y':2
}

# 打印两个字典相同的键
print(a.keys() & b.keys())

# 打印a字典有的键，而b字典没有的键
print(a.keys() - b.keys())

# 打印相同的键和值
print(a.items() & b.items())