# 新线程协程
import asyncio
import time
import threading
from threading import Thread

def start_loop(loop):
    print(threading.current_thread())
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def do_some_work(x):
    print(threading.current_thread())
    print('Waiting {}'.format(x))
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

start = time.time()
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()
print('TIME: {}'.format(time.time() - start))

ret1 = asyncio.run_coroutine_threadsafe(do_some_work(2), new_loop)
ret2 = asyncio.run_coroutine_threadsafe(do_some_work(3), new_loop)

print(ret1.result())
print(ret2.result())