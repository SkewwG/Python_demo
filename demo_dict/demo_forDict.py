# 与字典有关的计算问题(zip+sorted对字典的值进行操作)
prices = {
    'A':45.23,
    'B':612.78,
    'C':205.55,
    'D':37.20,
    'E':10.75
}

keys = prices.keys()
values = prices.values()

# 打印无序的字典
for i in prices:
    print(i,prices[i])

# 对字母进行排序
m = sorted(zip(keys,values))
print(m)

# 对数字进行排序
n = sorted(zip(values,keys))
print(n)