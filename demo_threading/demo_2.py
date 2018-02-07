#-*- coding:utf-8 -*-
import threading
import time

mu = threading.Lock()

def func():
    global task_start
    global task_num

    while task_start < task_num:
        if mu.acquire():
            if task_start < task_num:
                task_start += 1
                print('[+] {0}'.format(task_start))
            mu.release()

def threading_func():
    threads = []
    for i in range(5):
        print(i)
        t = threading.Thread(target=func)
        threads.append(t)

    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

if __name__ == '__main__':
    start_time = time.time()
    task_start = 0
    task_num = 100
    threading_func()
    end_time = time.time()
    times = end_time - start_time
    print('times : {0}'.format(times))