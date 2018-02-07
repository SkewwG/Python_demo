#例4:event实现进程间同步通信
import multiprocessing
import time

#event的方法有set（设置为True），clear（设置为False），is_set（查看当前状态）
def wait_for_event(e):
    print('wait_for_event:starting')
    e.wait()                                    #事件的默认状态为False，遇到wait阻塞，所以要等待事件的状态为True，才能往下执行
    print('wait_for_event:e.is_set()->',e.is_set())

def wait_for_event_timeout(e,t):
    print('wait_for_event_timeout:starting')
    print(time.ctime())
    e.wait(t)                                   #e.wait(2)的作用就是停2秒钟，和time.sleep相似的作用
    print(time.ctime())
    print('wait_for_event_timeout:e.is_set()->',e.is_set())

if __name__ == '__main__':
    event = multiprocessing.Event()
    m1 = multiprocessing.Process(target=wait_for_event,args=(event,))
    m2 = multiprocessing.Process(target=wait_for_event_timeout,args=(event,2))
    m1.start()
    m2.start()
    time.sleep(10)
    event.set()
    print("main:event is set")