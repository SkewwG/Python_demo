#例1.4：daemon程序对比结果,加daemon守护进程
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
    #daemon守护进程，主进程结束，子进程也就随之结束！
    p.daemon = True
    p.start()
    print('end!')

'''
设置了daemon守护进程
则只执行主进程
C:\Python34\python3.exe C:/Users/ske/Desktop/文件夹/py/demo/demo_process/demo_process4.2.py
end!
'''