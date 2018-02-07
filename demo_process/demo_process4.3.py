#例1.4：daemon程序对比结果,加daemon守护进程和join
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
    p.daemon = True
    p.start()
    #join先执行子进程，然后执行主进程
    p.join()
    print('end!')


'''
设置了守护进程daemon和join
先执行子进程，然后再执行主进程
C:\Python34\python3.exe C:/Users/ske/Desktop/文件夹/py/demo/demo_process/demo_process4.3.py
the time is  Tue Aug 22 21:54:22 2017
the time is  Tue Aug 22 21:54:25 2017
the time is  Tue Aug 22 21:54:28 2017
the time is  Tue Aug 22 21:54:31 2017
the time is  Tue Aug 22 21:54:34 2017
end!
'''