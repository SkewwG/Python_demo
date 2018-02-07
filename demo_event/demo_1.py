import threading
from queue import Queue

event = threading.Event()
event.set()


q = Queue(-1)


class multi_threading(threading.Thread):
    def __init__(self,num,q):
        threading.Thread.__init__(self)
        self.num = num
        self.q = q

    def run(self):
        while event.is_set():
            if self.q.empty():
                event.clear()
            else:
                print('[{}] crawl : {}'.format(self.num,q.get()))



def scan_thread():
    thread_num = 10
    threads = []
    for i in range(10000):
        q.put(i)


    for num in range(1,thread_num+1):
        t = multi_threading(num,q)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    scan_thread()