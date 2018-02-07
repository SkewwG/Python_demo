# 用指定的宽度来返回一个居中版的s，
# 如果需要的话，就用fillchar进行填充，默认是空格。但是不会对s进行截取。
# 即如果s的长度比width大，也不会对s进行截取。
'''
center(...)
    S.center(width[, fillchar]) -> str

    Return S centered in a string of length width. Padding is
    done using the specified fill character (default is a space)
'''
print(help(str.center))
a = 'asdfghjkl'
b = a.center(20, '-')               # 长度为20，a字符串居中，左右用数字5填充
print(b)                            # b = 55555asdfghjkl555555
