#例子1.3：将进程定义为类
import multiprocessing
import time

class ClockProcess(multiprocessing.Process):
    def __init__(self,interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        n = 5
        while n:
            print('the time is ',time.ctime())
            n -= 1
            time.sleep(3)

if __name__ == '__main__':
    processes = []
    for num in range(1,4):
        p = ClockProcess(3)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()