# 异步多进程

import aiohttp
import newspaper
import asyncio
import threading
import time
import datetime
import newspaper
import os

url = r'http://www.chinanews.com'
coroutine_num = 3  # 协程数目
coroutine_num_1 = coroutine_num - 1
category_num = 20  # 获取20个待爬取的新闻网址
headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

from concurrent.futures import ThreadPoolExecutor
t_executor = ThreadPoolExecutor(max_workers=coroutine_num)

from concurrent.futures import ProcessPoolExecutor
p_executor = ProcessPoolExecutor(max_workers=5)

# 打印时间
def now_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 获取20个待爬取的新闻网址
def get_categorys(url):
    qq_paper = newspaper.build(url)       # 返回构造的原对象， 而不是文章的下载或者解析
    categorys = []
    for category in qq_paper.category_urls()[:category_num]:           # 获取子域
        categorys.append(category)
    return categorys

# 获取网站url
def get_url(category_url):
    t_id = threading.current_thread().ident
    print('[t{}] [{}]-> {}'.format(t_id, now_time(), category_url))
    category_url_paper = newspaper.build(category_url)
    article_urls = []           # 存放url
    for article in category_url_paper.articles[:10]:  # 获取文章地址
        article_url = article.url.strip()
        # print('[{}] -> {}'.format(t_id, article_url))
        article_urls.append(article_url)
    print(t_id, category_url, article_urls)
    return article_urls

async def down_html(article_urls):
    t_id = threading.current_thread().ident
    for article_url in article_urls:
        async with aiohttp.ClientSession() as session:
            async with session.get(article_url, headers=headers) as res:
                # code = res.status
                print('[t{}] [{}]-> {}'.format(t_id, now_time(), article_url))
                text = await res.text()
                return text


async def main():
    # loop1 = asyncio.get_event_loop()
    article_urls_result = [loop.run_in_executor(t_executor, get_url, category_url) for category_url in categorys]
    print(article_urls_result)
    for a in article_urls_result:
        article_urls = await a
        await down_html(article_urls)




        # t_id, category_url, article_urls = result
        # print('[{}] [{}]-> {}'.format(t_id, now_time(), category_url))


if __name__ == '__main__':



    # categorys = get_categorys(url)
    categorys = ['http://www.gd.chinanews.com', 'http://www.ha.chinanews.com', 'http://www.chinanews.com/',
     'http://www.sd.chinanews.com', 'http://finance.chinanews.com', 'http://health.chinanews.com',
     'http://www.bt.chinanews.com', 'http://www.hn.chinanews.com', 'http://www.chinanews.com',
     'http://house.chinanews.com', 'http://sports.chinanews.com', 'http://www.hb.chinanews.com',
     'http://www.qh.chinanews.com', 'http://life.chinanews.com', 'http://www.hi.chinanews.com',
     'http://www.js.chinanews.com', 'http://www.jx.chinanews.com', 'http://business.chinanews.com',
     'http://auto.chinanews.com', 'http://channel.chinanews.com']
    print('[categorys] : {}'.format(categorys))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


