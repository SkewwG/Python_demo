# 把@asyncio.coroutine替换为async；
# 把yield from替换为await。



import time
import threading
import asyncio

async def hello():
    print(threading.current_thread(), time.time())
    r = await asyncio.sleep(1)
    print(threading.current_thread(), time.time())

loop = asyncio.get_event_loop()     # 创建一个事件循环
loop.run_until_complete(hello())        # 将协程注册到事件循环，并启动事件循环
loop.close()