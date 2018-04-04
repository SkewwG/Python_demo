# 多进程+异步爬取网站标题
import multiprocessing
import asyncio
import aiohttp
import os
import time
from termcolor import cprint
from bs4 import BeautifulSoup

event = multiprocessing.Event()
event.set()
q = multiprocessing.Queue(-1)
headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
ProcessNum = 3
asyncNum = 10


def get_q():
    with open(r'C:\Users\Asus\Desktop\py\py3\single\collectBackGround\txtCut\test.txt', encoding='utf-8') as f:
        for each in f.readlines():
            q.put(each.strip())


def scan(q):
    processes = []
    for i in range(1, ProcessNum+1):
        p = multiProcess(q)
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


class multiProcess(multiprocessing.Process):
    def __init__(self, q):
        multiprocessing.Process.__init__(self)
        self.q = q
        self.urls = []

    def run(self):
        while event.is_set():
            if self.q.empty():
                event.clear()
            else:
                for _ in range(asyncNum):
                    self.urls.append(self.q.get())
                self.asy(self.urls)
                self.urls = []


    # 异步请求
    async def req(self, url):
        pid = os.getpid()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as res:
                    code = res.status
                    print('[{}][{}] : {}'.format(pid, url, code))
                    ret = await res.text()
                    return [ret, code, url]
        except Exception as e:
            cprint('[{}]{} get text error'.format(pid, url), 'green')
            return None

    # 异步
    def asy(self, urls):
        loop = asyncio.get_event_loop()     # 创建一个事件循环，
        tasks = [self.req(url) for url in urls]     # 创建多个协程的列表，
        rets = loop.run_until_complete(asyncio.gather(*tasks))      # 将这些协程注册到事件循环中。
        for ret in rets:
            if ret and ret[0]:
                title = self.search_title(ret[0])
                success = [ret[1], ret[2], title]
                cprint(success, 'red')
                self.save(success)


    def search_title(self, ret):
        try:
            soup = BeautifulSoup(ret, 'html.parser')
            Title = soup.title.string.strip()  # 利用bs4获取title内容，用strip去掉两边空格符
            return Title
        except Exception as e:
            return ''

    def save(self, success):
        with open('ret.txt', 'at', encoding='utf-8') as f:
            f.writelines(str(success) + '\n')

if __name__ == '__main__':
    start = time.time()
    get_q()
    scan(q)
    cost_time = time.time() - start
    print(cost_time)