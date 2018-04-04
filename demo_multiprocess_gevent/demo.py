# 多进程+协程demo

import multiprocessing
import gevent
from gevent import monkey
monkey.patch_all()
import requests
from bs4 import BeautifulSoup


event = multiprocessing.Event()
event.set()
q = multiprocessing.Queue(-1)                           #队列必须使用多进程的队列，使用queue模块会报错

class multi_Process(multiprocessing.Process):
    def __init__(self,q,num):
        multiprocessing.Process.__init__(self)
        self.q = q
        self.num = num
        self.j = 0

    # 多进程完成打印100份26个阿拉伯字母
    def run(self):
        while event.is_set():
            if self.q.empty():
                event.clear()
            else:
                self.search()

    #
    def search(self, flag=5):
        i = 0
        url_list = []
        while True:
            self.j += 1
            if self.q.empty():
                if url_list:    # 过滤url_list为空
                    print(self.num, url_list, len(url_list))
                    #self.gev(url_list)

                break

            else:
                url = self.q.get()
                # print('[p{}] {}'.format(self.num, url))
                i += 1
                url_list.append(url)
                #print(self.num, url_list, len(url_list))
                if i == flag:
                    #self.gev(url_list)
                    print(self.num, url_list, len(url_list))
                    url_list = []
                    i = 0




    # 协程请求网址
    def gev(self, url_list):
        jobs = [gevent.spawn(self.search_title, url) for url in url_list]
        gevent.joinall(jobs)

    def search_title(self, url):
        try:
            url = 'http://' + url
            print('[{}][p{}] : {}'.format(self.j, self.num, url))
            response = requests.get(url=url, timeout=3)  # allow_redirects=False防止重定向到正常页面,过滤绝大部分错误页面
            print('[{}][{}]curl : {}'.format(self.j, response.status_code, url))
            if response.status_code == 200:
                response_text = response.content
                soup = BeautifulSoup(response_text, 'html.parser')
                Title = soup.title.string.strip()  # 利用bs4获取title内容，用strip去掉两边空格符
                print('[{}][p{}] : {}'.format(self.j, self.num, Title))

            else:
                print('[-p{}] : {} is not requests!'.format(self.num, url))
        except Exception as e:
            print(e)




def scan_thread(q):
    processes = []
    process_num = 3
    for num in range(1,process_num+1):
        p = multi_Process(q, num)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()


import gevent
from gevent import monkey
monkey.patch_all()

def get_q():
    with open(r'C:\Users\Asus\Desktop\py\py3\single\collectBackGround\txtCut\test.txt', 'rt') as f:
        for each in f.readlines():
            #print(each.strip())
            q.put(each.strip())


if __name__ == '__main__':
    get_q()
    print(type(q))
    print(q.qsize())
    print(dir(q))
    print('q.empty : {}'.format(q.empty()))
    print('q.size : {}'.format(q.qsize()))
    print(q.get())
    # while not q.empty():
    #     print(q.get())
    #scan_thread(q)
    print('done')
