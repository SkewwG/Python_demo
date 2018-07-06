import asyncio
import requests
from bs4 import BeautifulSoup
import chardet
from threading import current_thread
import datetime

# 打印时间
def nowTime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 定义异步方法：获取标题
async def searchTitle(url):
    html_doc = await getHtml(url)
    try:
        soup = BeautifulSoup(html_doc, 'html.parser')
        Title = soup.title.string.strip()                   # 利用bs4获取title内容，用strip去掉两边空格符
        return current_thread(), url, Title
    except Exception as e:
        return None

# 定义异步方法：获取网页源码
async def getHtml(url):
    print('[{}] : request {}'.format(nowTime(), url))
    res = requests.get(url, timeout=5)
    # print('[{}] : {} return response'.format(nowTime(), url))
    try:
        cont = res.content
        # 获取网页的编码格式
        charset = chardet.detect(cont)['encoding']
        # 对各种编码情况进行判断
        html_doc = cont.decode(charset)
    except Exception as e:
        html_doc = res.text
    return html_doc

if __name__ == '__main__':
    urls = []                   # 存放coroutineNums数量的url
    coroutineNums = 10          # 定义协程数
    coroutineNums_1 = coroutineNums - 1
    loop = asyncio.get_event_loop()     # 创建一个事件循环

    with open('urls.txt', 'rt') as f:
        for i, url in enumerate(f):             # 不用f.readlines(),因为f是生成器，用for迭代取出每个值。这样避免过度占用内存
            if i % coroutineNums != coroutineNums_1:        # 每coroutineNums个一组
                urls.append(url.strip())
            else:
                urls.append(url.strip())
                print(urls)                     # 打印每次请求的url
                tasks = [searchTitle(url) for url in urls]      # 创建多个协程的列表
                results = loop.run_until_complete(asyncio.gather(*tasks))       # run_until_complete 参数是一个futrue对象。但是如果当传入一个协程，其内部会自动封装成task，task是Future的子类。 将协程注册到事件循环，并启动事件循环。
                titles = filter(lambda title : title, results)        # 使用flter和lambda 过滤了结果为None的值
                for title in titles:          # 打印标题
                    print('[{}] : {}'.format(nowTime(), title))
                print('-'*50)
                del urls[:]         # 清除缓存
