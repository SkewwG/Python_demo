# asyncio实现并发，就需要多个协程来完成任务，每当有任务阻塞的时候就await，然后其他协程继续工作。
# 创建多个协程的列表，然后将这些协程注册到事件循环中。
import aiohttp
import asyncio

async def func(url):    # async定义一个协程
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            print('curl : [{}]'.format(url))
            await asyncio.sleep(1)      # 模拟IO操作或者网络请求
            return '[{}] sleep 1s'.format(url)

urls = ['http://0xsafe.org/', 'https://www.bugbank.cn/', 'http://sec.baidu.com/views/main/index.html#home',
        'http://security.jd.com/', 'https://sec.ctrip.com/', 'http://sec.sina.com.cn/',
        'http://www.robam.com', 'http://www.ximalaya.com', 'http://www.ztgame.com/', 'http://www.omegatravel.net',
        'http://www.zhiye.com', 'http://www.tita.com', 'http://www.beisen.com']

# task = func('http://0xsafe.org/')
# print(type(task))       # coroutine

loop = asyncio.get_event_loop()
tasks = [func(url) for url in urls]
rets = loop.run_until_complete(asyncio.gather(*tasks)) # gather传递多参数
print(rets)
loop.close()
