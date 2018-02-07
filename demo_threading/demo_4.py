#-*- coding:utf-8 -*-
#多线程+线程锁+线程数
import threading
import time
import socket



mu = threading.Lock()


class MyThread(threading.Thread):

    def scanPort(self):
        global tgtHost
        global tgtPort
        if mu.acquire():
            try:
                socket.setdefaulttimeout(8)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((tgtHost, tgtPort))
                print('[+] {0}:{1} open'.format(tgtHost, tgtPort))
            except Exception as e:
                s.close()
                print('[-] {0} closed error:{1}'.format(tgtHost, str(e)))
            s.close()
            mu.release()

    def run(self):
        self.scanPort()



def threading_demo():
    threads = []
    for i in range(10):
        t = MyThread()
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    tgtHost = '192.168.1.100'
    tgtPort = 100



    start_time = time.time()
    threading_demo()
    end_time = time.time()
    times = end_time - start_time
    print('times:{0}'.format(times))

