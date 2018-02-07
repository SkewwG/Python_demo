#-*- coding:utf-8 -*-

import threading        #多线程模块
import socket           #套接字模块
import queue            #队列模块
import time             #计时

lock = threading.Lock()                                                                    #线程锁

class scanThread(threading.Thread):
    def scan(self,tgtHost,tgtPort,num):
        global lock
        socket.setdefaulttimeout(2)
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        address = (tgtHost,tgtPort)

        try:
            sock.connect(address)
            print('[+] 第{0}条线程 {1} : open[{2}] '.format(num,tgtHost,tgtPort))
        except Exception as e:
            sock.close()
            print('[-] 第{0}条线程 {1} : Port[{2}] closed  error : {3}'.format(num,tgtHost,tgtPort,e))
        sock.close()


class scanThread_multi(scanThread):
    def __init__(self,num):
        super(scanThread_multi,self).__init__()
        self.num = num

    def run(self):
        global results

        for i in range(results[0],results[1]+1):
            tgtHost = NumtoIp(i)
            results[0] += 1
            for j in range(results[2],results[3]+1):
                self.scan(tgtHost,j,self.num)


def scan_threading(results):                                                                       #多线程
    threads = []
    for i in range(results[4]):
        num = i
        print('num:',num)
        t = scanThread_multi(num)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()




def IptoNum(Host):
    splitHostList = [int(hostIp) for hostIp in Host.split('.')]             #splitHostList为IP分割后的IP列表
    return sum([splitHostList[i] << [24,16,8,0][i] for i in range(4)])   #HostNum位IP转为为10进制后的结果


def NumtoIp(HostNum):
    HostIp = '.'.join([str(HostNum >> j & 0xff) for j in [24,16,8,0]])
    return HostIp


if __name__ == '__main__':
    tgtIpStart, tgtIpEnd = input('[start_Ip-end_Ip]>>>').split('-')                         # 192.168.1.100-192.168.1.100
    tgtPortStart, tgtPortEnd = map(int, input('[start_Port-end_Port]>>>').split('-'))       # 1-1000             map()将输入的字符串转换为int
    threadingNum = int(input('[the num of threading]>>>'))                                  # 线程数
    results = [IptoNum(tgtIpStart),IptoNum(tgtIpEnd),tgtPortStart, tgtPortEnd,threadingNum]


    scan_threading(results)