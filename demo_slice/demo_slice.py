l = [i for i in range(100)]

a = slice(20,22)                            # slice()函数创建一个切片对象
print(l[a])
print('start {}'.format(a.start))
print('end {}'.format(a.stop))
print('step {}'.format(a.step))