import threading
import time
import socket




def IptoNum(Host):
    splitHostList = [int(hostIp) for hostIp in Host.split('.')]                         #splitHostList为IP分割后的IP列表
    return sum([splitHostList[i] << [24,16,8,0][i] for i in range(4)])                  #HostNum位IP转为为10进制后的结果


def NumtoIp(HostNum):
    HostIp = '.'.join([str(HostNum >> j & 0xff) for j in [24,16,8,0]])
    return HostIp

def portScan(tgtHost,tgtPort,num):                                                      #端口扫描
    socket.setdefaulttimeout(0.01)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (tgtHost, tgtPort)
    try:
        sock.connect(address)
        print('[+] 第{0}条线程 {1} : open[{2}] '.format(num, tgtHost, tgtPort))
    except Exception as e:
        sock.close()
        print('[-] 第{0}条线程 {1} : Port[{2}] closed  error : {3}'.format(num, tgtHost, tgtPort, e))
    sock.close()


def func(num):
    global ipStartNum,ipEndNum,portStart,portEnd,lock
    if portStart != portEnd:                                                            #多IP多端口，单IP多端口
        while ipStartNum < ipEndNum:                                                    #继续用while语句，如果用for语句是多个线程都执行同样的语句，而不是一个接一个的执行
            while portStart < portEnd:
                if lock.acquire():
                    if (ipStartNum < ipEndNum) and (portStart < portEnd):
                        tgtHost = NumtoIp(ipStartNum)
                        tgtPort = portStart
                        portScan(tgtHost, tgtPort, num)
                        portStart += 1
                    lock.release()
            portStart = portStart_temp                                                  #端口恢复为start
            ipStartNum += 1
    else:                                                                               #多IP单端口，单IP单端口
        while ipStartNum < ipEndNum:
            if lock.acquire():
                if ipStartNum < ipEndNum:
                    tgtHost = NumtoIp(ipStartNum)
                    tgtPort = portStart
                    portScan(tgtHost, tgtPort, num)
                lock.release()
            ipStartNum += 1




lock = threading.Lock()
threads = []
task_start = 0
task_num = 100
ipStart = '10.228.0.34'
ipEnd = '10.228.0.34'
portStart = 445
portEnd = 445
portStart_temp = portStart


if __name__ == '__main__':
    ipStartNum = IptoNum(ipStart)
    ipEndNum = IptoNum(ipEnd)+1

    start_time = time.time()
    for i in range(100):                                                            #线程数
        num = i
        t = threading.Thread(target=func,args=(num,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end_time = time.time()
    times = end_time-start_time
    print('times:',times)
