# run_until_complete 和 run_forever的区别

# run_until_complete
import asyncio
import aiohttp
import functools

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

def callback(t, future):
    loop.stop()

tasks = [func(url) for url in urls]
loop = asyncio.get_event_loop()
futus = asyncio.gather(*tasks)
futus.add_done_callback(functools.partial(callback, loop)) # 用 gather 把多个协程合并成一个 future，并添加回调，然后在回调里再去停止 loop。
loop.run_forever()
