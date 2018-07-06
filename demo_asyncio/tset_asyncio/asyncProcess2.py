# 多进程+异步爬取网站标题
import multiprocessing
import asyncio
import aiohttp
import os
import time
from termcolor import cprint
from bs4 import BeautifulSoup
import chardet
import traceback
import codecs


event = multiprocessing.Event()
event.set()
q = multiprocessing.Queue(-1)
headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
ProcessNum = 3
asyncNum = 10


async def req(url):
    pid = os.getpid()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as res:
                code = res.status
                #print(dir(res))
                #encoding = res.get_encoding()
                #print(encoding)
                html_doc = await res.text
                # ret = await res.read()
                # html_doc = ret.decode(encoding, 'ignore')
                return [html_doc, code, url]
    except Exception as e:
        #cprint('[{}]{} get text error: {}'.format(pid, url, traceback), 'green')
        traceback.print_exc(e)
        #traceback.print_exc(e)
        return None

def search_title(html_doc):
    try:
        soup = BeautifulSoup(html_doc, 'html.parser')
        Title = soup.title.string.strip()  # 利用bs4获取title内容，用strip去掉两边空格符
        return Title
    except Exception as e:
        return ''

if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # 创建一个事件循环，
    urls = []
    with open(r'urls2.txt', encoding='utf-8') as f:
        for i, each in enumerate(f):
            if i % 10 != 9:
            # if i % 2 != 1:
                urls.append(each.strip())
                i += 1
            else:
                print(urls)
                tasks = [req(url) for url in urls]  # 创建多个协程的列表，
                rets = loop.run_until_complete(asyncio.gather(*tasks))  # 将这些协程注册到事件循环中。
                for ret in rets:
                    if ret and ret[0]:
                        title = search_title(ret[0])
                        success = [ret[1], ret[2], title]
                        cprint(success, 'red')
                urls = []

