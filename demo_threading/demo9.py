import threading
from queue import Queue
from threading import current_thread
import time

event = threading.Event()
event.set()
q = Queue(-1)
q2 = Queue(-1)
class multiThread(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q


    def run(self):
        while event.is_set():
            if self.q.empty():
                event.clear()
            else:
                i = self.q.get()
                print(current_thread(), self.q, i)
                time.sleep(1)

def scan_thread(q):
    threads = []
    thread_num = 3
    for i in range(1, thread_num+1):
        t = multiThread(q)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


if __name__ == '__main__':
    for i in range(10):
        q.put(i)
    scan_thread(q)
