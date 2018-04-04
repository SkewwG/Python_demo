# 通信

def demo1():
    r = 0
    while True:
        n = yield r
        print('rec : {}'.format(n))

def demo2(c):
    c.__next__()
    n = 0
    while n < 5:
        print('send : {}'.format(n))
        c.send(n)
        n += 1
    c.close()



c = demo1()
demo2(c)