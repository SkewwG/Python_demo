#协程+多进程

import multiprocessing
import gevent
import time
from multiprocessing import Pool
import os

event = multiprocessing.Event()
event.set()
q = multiprocessing.Queue(-1)

class multi_Process(multiprocessing.Process):
    def __init__(self,q,num):
        multiprocessing.Process.__init__(self)
        self.q = q
        self.num = num
        self.pid = os.getpid()

    # 多进程完成打印100份26个阿拉伯字母
    def run(self):
        while event.is_set():
            if self.q.empty():
                break
            else:
                digit = self.q.get()
                self.gev(digit)
                time.sleep(1)

    # 打印阿拉伯字母
    def print_alpha(self,alpha,digit):
        print('[t{}] digit : [{}] alpha : [{}]'.format(self.pid,digit,chr(alpha)))

    # 协程打印26个阿拉伯字母
    def gev(self,digit):
        jobs = [gevent.spawn(self.print_alpha,alpha,digit) for alpha in range(97,123)]
        gevent.joinall(jobs)

def scan_thread():
    processes = []
    process_num = 10
    for num in range(1,process_num+1):
        p = multi_Process(q,num)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

def get_q():
    for i in range(1,100):
        q.put(i)

if __name__ == '__main__':
    get_q()
    scan_thread()