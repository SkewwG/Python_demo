# 协程嵌套
import asyncio
import aiohttp

urls = ['http://0xsafe.org/', 'https://www.bugbank.cn/', 'http://sec.baidu.com/views/main/index.html#home',
        'http://security.jd.com/', 'https://sec.ctrip.com/', 'http://sec.sina.com.cn/',
        'http://www.robam.com', 'http://www.ximalaya.com', 'http://www.ztgame.com/', 'http://www.omegatravel.net',
        'http://www.zhiye.com', 'http://www.tita.com', 'http://www.beisen.com']

async def func(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            print('[{}] : {}'.format(res.status, res.url))
            await asyncio.sleep(1)
            return '[{}] : sleep 1'.format(url)

async def main():
    tasks = [func(url) for url in urls]

    dones, pending = await asyncio.wait(tasks)
    for task in dones:
        print('task ret :{}'.format(task.result()))

    # 如果使用的是 asyncio.gather创建协程对象，那么await的返回值就是协程运行的结果。
    # rets = await asyncio.gather(*tasks)
    # for ret in rets:
    #     print('task ret :{}'.format(ret))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())