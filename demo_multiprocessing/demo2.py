from multiprocessing import Pool
import os, time

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(5)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())       # 打印进程的ID
    p = Pool(processes=10)                          # 进程池，如果不设置，就默认为计算机的CPU个数
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))    # 异步
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()                                        # 等待所有子进程结束
    print('All subprocesses done.')