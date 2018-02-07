#协程爬取国外代理IP，并筛选出有效IP
from bs4 import BeautifulSoup
import requests
import os
import gevent
from gevent import monkey; monkey.patch_all()            #monkey猴子补丁，如果不打猴子补丁，在协程访问网站是不会同时进行的，而是一个个以此访问。这样就达不到高效率
import threading
from queue import Queue

event = threading.Event()
event.set()
q_proxies = Queue(-1)

path = os.getcwd()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}

#获取代理IP
def get_ip_list(each_ret):
    soup = BeautifulSoup(each_ret,'html.parser')
    ips = soup.find_all('tr')
    proxy_list = []
    for i in range(1,len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        proxy_list.append('http://' + tds[0].string + ':' + tds[1].string)
    return proxy_list

# 获取单页内容
def get_eachPageText(digit):
    url = r'http://www.kuaidaili.com/free/outha/{}/'.format(digit)
    response = requests.get(url=url, headers=headers)
    ret = response.text
    return ret

# 协程获取每个页面内容
def gev_getText():
    jobs = [gevent.spawn(get_eachPageText,digit) for digit in range(1,100)]
    gevent.joinall(jobs)
    demo_q = Queue(-1)
    for job in jobs:
        each_ret = job.value
        #将爬取的IP和端口存入队列里
        ret = get_ip_list(each_ret)
        q_proxies.put(ret)
        demo_q.put(ret)

    while not demo_q.empty():
         print(demo_q.get())

    return q_proxies

#多线程类
class multi_thread(threading.Thread):
    def __init__(self,q,num):
        threading.Thread.__init__(self)
        self.q = q
        self.num = num

    def run(self):
        while event.is_set():
            if self.q.empty():
                break
            else:
                proxies_l = self.q.get()          #取出的数据是每页的所有IP，是一个列表
                self.gev(proxies_l)

    #协程扫描代理IP是否有效
    def gev(self,proxies_l):
        jobs = [gevent.spawn(self.check_IP,pro) for pro in proxies_l]
        gevent.joinall(jobs)

    #检查IP有效性
    def check_IP(self,pro):
        try:
            print('[*{}] test : {}'.format(self.num,pro))
            url = r'http://www.whatismyip.com.tw/'
            proxies = {'http':pro}
            response = requests.get(url=url,headers=headers,proxies=proxies)
            ret = response.text
            soup = BeautifulSoup(ret,'html.parser')
            ip = soup.find('b')
            print('[+{}] test {} success : {}'.format(self.num,pro,ip.string))
            self.save(pro)
        except Exception as e:
            pass

    def save(self,pro):
        with open(path + r'/valid.txt','at') as f:
            f.writelines(pro+'\n')


#多线程方法
def scan_thread():
    threads = []
    thread_num = 10
    for num in range(1,thread_num+1):
        t = multi_thread(q_proxies,num)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    gev_getText()
    scan_thread()
