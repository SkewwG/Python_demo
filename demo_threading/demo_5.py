#-*- coding:utf-8 -*-
#多线程+线程锁
import threading
import time


start_task = 0
task_num = 1000000
mu = threading.Lock()   ###通过工厂方法获取一个新的锁对象
class MyThread(threading.Thread):   ###类MyThread继承基类threading.Thread
    def run(self):  ##线程启动的入口函数，子类需重写
        global start_task
        global mu
        global start_task
        while start_task < task_num:    ##如果任务没有完成，则继续
            if mu.acquire():    ##加锁
                if start_task < task_num:
                    start_task = start_task + 1
                mu.release()    ##释放锁
def test():
    thread_all = []
    for i in range(3):  ##for循环创建6个线程
        t = MyThread()  ##创建线程
        thread_all.append(t)
        t.start()   ###启动线程
    for i in range(3):
        thread_all[i].join()    ##等待线程结束
if __name__ == "__main__":
    start_time = time.time()
    test()
    end_time = time.time()
    times = end_time - start_time
    print('times:{0}'.format(times))