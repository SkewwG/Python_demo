#多进程模板
import multiprocessing
import time

event = multiprocessing.Event()
event.set()
q = multiprocessing.Queue(-1)                           #队列必须使用多进程的队列，使用queue模块会报错

#自定义多进程类
class multi_Process(multiprocessing.Process):
    def __init__(self,q,num):
        multiprocessing.Process.__init__(self)
        self.q = q
        self.num = num

    def run(self):
        while event.is_set():
            if self.q.empty():
                break
            else:
                digit = self.q.get()
                self.print_digit(self.num,digit)

    def print_digit(self,num,digit):
        print('[t{}] scan {}'.format(num,digit))
        time.sleep(1)

#多进程方法
def scan_thread(q):
    processes = []
    processes_num = 3
    for num in range(1,processes_num+1):
        p = multi_Process(q,num)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

#获取队列
def get_q():
    for i in range(1000):
        q.put(i)

if __name__ == '__main__':
    get_q()
    scan_thread(q)
