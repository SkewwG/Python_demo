# 协程
'''
1、先执行c.__next__()
2、程序跳到consumer运行到n = yield r，返回的是r，r为''
3、程序回到produce执行到r = c.send(n)，发送值为1的n给n = yield r语句。yield的作用是接收send发送过来的n值
4、程序执行了r = '200 OK'，在while语句里循环执行到n = yield r语句。发送r给produce的r = c.send(n)语句
5、程序回到produce的r = c.send(n)语句，send的作用是使r接收yield发送过来的r值
'''
import time

def consumer():
    r = ''                                                  #为了n = yield r该语句能够发送r，且没有实际作用。所以设置一个空的变量r
    while True:
        n = yield r                                         #yield的作用是发送r接收n
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(3)
        r = '200 OK'

def produce(c):
    c.__next__()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)                                       #send的作用是发送n接收r
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__=='__main__':
    c = consumer()
    produce(c)