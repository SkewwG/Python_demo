import threading
import time



lock = threading.Lock()

class threading_demo(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        #super(threading_demo,self).__init__()
        self.num = num


    def run(self):
        global lock,start,end
        while start < end:
            if lock.acquire():
                if start < end:
                    print('thread[{}] : {}'.format(self.num,start))
                    start += 1
                    time.sleep(0.1)
                lock.release()



def scan_thread():
    thread_num = 10
    threads = []




    for each in range(1,thread_num):
        t = threading_demo(each)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    start = 0
    end = 100
    scan_thread()