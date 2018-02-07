#-*- coding:utf-8 -*-
import threading
import time
import socket

def portScan():
    tgtHost = '192.168.1.100'
    tgtPort = 81
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((tgtHost,tgtPort))
        print('[+] {0} {1} open'.format(tgtHost,tgtPort))
    except Exception as e:
        print('[-] {0} {1} closed : {2}'.format(tgtHost,tgtPort,e))
        pass

def threading_demo():
    threads = []
    for i in range(5):
        print(i)
        t = threading.Thread(target=portScan)
        threads.append(t)

    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()


if __name__ == '__main__':




    
    start_time = time.time()
    threading_demo()
    end_time = time.time()
    print('times : {0}'.format(end_time-start_time))