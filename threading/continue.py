#可以看到即使某个子线程退出了，之后仍然会继续调用该子线程运行脚本，并不会减少线程数目！
import threading
from queue import Queue
import time


event = threading.Event()
event.set()
q = Queue(-1)



class multiThread(threading.Thread):
    def __init__(self,q,num):
        threading.Thread.__init__(self)
        self.q = q
        self.num = num

    def run(self):
        while event.is_set():
            if self.q.empty():
                break
            else:
                try:
                    digit = self.q.get()
                    if digit % 3 == 0:
                        print('[-]t{} : {} exit'.format(self.num, digit))
                        continue
                    else:
                        print('[+]t{} : {}'.format(self.num,digit))
                    time.sleep(5)
                except:
                    pass

def scan_thread():
    threads = []
    thread_num = 5
    for num in range(1,thread_num+1):
        t = multiThread(q,num)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def put_q():
    for i in range(1,100):
        q.put(i)

if __name__ == '__main__':
    put_q()
    scan_thread()
