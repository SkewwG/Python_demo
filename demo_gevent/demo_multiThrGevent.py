#协程+多线程

import gevent
import threading
from queue import Queue

event = threading.Event()
event.set()
q = Queue(-1)
class multi_thread(threading.Thread):
    def __init__(self,q,num):
        threading.Thread.__init__(self)
        self.q = q
        self.num = num

    #打印阿拉伯字母
    def printAlpha(self,alpha,num,digit):
        print('[t{}] digit : [{}] alpha : [{}]'.format(num,digit,chr(alpha)))

    #协程打印26个阿拉伯字母
    def gev(self,num,digit):
        jobs = [gevent.spawn(self.printAlpha,i,num,digit) for i in range(97,123)]
        gevent.joinall(jobs)

    #多线程完成打印100份26个阿拉伯字母
    def run(self):
        while event.is_set():
            if self.q.empty():
                break
            else:
                digit = q.get()
                self.gev(self.num,digit)

def scan_thread(q):
    threads = []
    thread_num = 3
    for num in range(1,thread_num+1):
        t = multi_thread(q,num)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def get_q():
    for i in range(100):
        q.put(i)
    return q

if __name__ == '__main__':
    q = get_q()
    scan_thread(q)