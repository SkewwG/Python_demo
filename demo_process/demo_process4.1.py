#例1.4：daemon程序对比结果,不加daemon守护进程
import multiprocessing
import time

def worker(interval):
    n = 5
    while n :
        print('the time is ',time.ctime())
        time.sleep(3)
        n -= 1

if __name__ == '__main__':
    p = multiprocessing.Process(target=worker,args=(3,))
    p.start()
    print('end!')

'''
没开daemon守护进程和join，则执行完主进程后，在执行子进程
C:\Python34\python3.exe C:/Users/ske/Desktop/文件夹/py/demo/demo_process/demo_process4.1.py
end!
the time is  Tue Aug 22 21:52:41 2017
the time is  Tue Aug 22 21:52:44 2017
the time is  Tue Aug 22 21:52:47 2017
the time is  Tue Aug 22 21:52:50 2017
the time is  Tue Aug 22 21:52:53 2017
'''