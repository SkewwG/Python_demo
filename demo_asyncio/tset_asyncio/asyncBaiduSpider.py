import requests
import asyncio
import re
from urllib.parse import quote
import aiohttp
import time

# def keyword(kw,page=1):
#     kw = quote(kw)
#     header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"}
#     url = 'https://www.baidu.com/s?wd=%s&pn=%s0'%(kw,page-1)
#     req = requests.get(url,headers=header)
#     res = re.findall(r'<a target="_blank" href="(\S+)" class="c-showurl"',req.text)
#     return list(set(res))
#
#
# tasks = [scanPort(url) for url in urls]  # 创建多个协程的列表，
# rets = loop.run_until_complete(asyncio.gather(*tasks))  # 将这些协程注册到事件循环中。

# 正则匹配出每一页的百度跳转链接
def baidu_location(keyword, pages):
    keyword = quote(keyword)
    for page in range(pages):
        eachUrl = 'https://www.baidu.com/s?wd=%s&pn=%s0'%(keyword,page-1)
        res = requests.get(url=eachUrl, headers=headers, timeout=5)
        return list(set(re.findall(r'<a target="_blank" href="(\S+)" class="c-showurl"',res.text)))

async def location2url(Lurl):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(Lurl, headers=headers, timeout=5) as res:
                print('test:', Lurl)
                time.sleep(3)
                url = res.url
                print('[+]:', url)
                return url
    except Exception as e:
        return ''

if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"}
    keyword = r'inurl:/index.php?m=content&c=index&a=show&catid=17&id='
    pages = 1
    loop = asyncio.get_event_loop()
    LocationUrls = baidu_location(keyword, pages)
    print('LocationUrls:', LocationUrls)
    tasks = [location2url(Lurl) for Lurl in LocationUrls]
    rets = loop.run_until_complete(asyncio.wait(tasks))
    print('rets:', rets)
    for ret in rets[0]:
        print('ret:', ret.result())


