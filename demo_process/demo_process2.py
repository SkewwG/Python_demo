#创建函数并将其作为多个进程
import multiprocessing
import time

def worker_1(interval):
    print("worker_1：",time.ctime())
    time.sleep(interval)
    print("end worker_1")

def worker_2(interval):
    print("worker_2：",time.ctime())
    time.sleep(interval)
    print("end worker_2")

def worker_3(interval):
    print("worker_3：",time.ctime())
    time.sleep(interval)
    print("end worker_3")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker_1, args = (2,))
    p2 = multiprocessing.Process(target = worker_2, args = (3,))
    p3 = multiprocessing.Process(target = worker_3, args = (4,))

    p1.start()
    p2.start()
    p3.start()

    print("The number of CPU is:" + str(multiprocessing.cpu_count()))       #multiprocessing.cpu_count()CPU的个数
    for p in multiprocessing.active_children():                             #multiprocessing.active_children()进程数目
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))           #p.name进程名，p.pid进程ID
    print("END!!!!!!!!!!!!!!!!!")