#协程例子
import gevent
import time

def test0():
    print('start0 :',time.ctime())
    #gevent.sleep(0)                 #睡0秒虽然相当于没有睡，但也在start1,2,3,4后面。但却也是同时进行的
    print('end0 :',time.ctime())

def test1():
    print('start1 :',time.ctime())
    #gevent.sleep(1)                 #睡一秒，相当于阻塞了一秒
    print('end1 :',time.ctime())

def test2():
    print('start2 :',time.ctime())
    #gevent.sleep(2)
    print('end2 :',time.ctime())

def test3():
    print('start3 :',time.ctime())
    #gevent.sleep(3)
    print('end3 :',time.ctime())

def test4():
    print('start4 :',time.ctime())
    #gevent.sleep(4)
    print('end4 :',time.ctime())

#gevent.joinall()方法会等待所有传入的greenlet协程运行结束后再退出
gevent.joinall([
    gevent.spawn(test0),        #gevent.spawn()方法创建一个新的greenlet协程对象，并运行它。
    gevent.spawn(test1),
    gevent.spawn(test2),
    gevent.spawn(test3),
    gevent.spawn(test4),
])