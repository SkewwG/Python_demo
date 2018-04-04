'''
创建task后，task在加入事件循环之前是pending状态，因为do_some_work中没有耗时的阻塞操作，task很快就执行完毕了。
后面打印的finished状态。

asyncio.ensure_future(coroutine) 和 loop.create_task(coroutine)都可以创建一个task，
run_until_complete的参数是一个futrue对象。当传入一个协程，其内部会自动封装成task，task是Future的子类。
isinstance(task, asyncio.Future)将会输出True。
'''
import asyncio
import threading
import time

@asyncio.coroutine
def do_some_work():
    print(threading.current_thread(), time.time())
    r = yield from asyncio.sleep(1)
    print(threading.current_thread(), time.time())

loop = asyncio.get_event_loop()
task = loop.create_task(do_some_work())    # 创建一个task
print(task) # <Task pending coro=<do_some_work() running at C:/Users/Asus/Desktop/py/demo/Python_demo/demo_asyncio/demo2.py:11>>
print(type(task))
loop.run_until_complete(task)
print(task) # <Task finished coro=<do_some_work() done, defined at C:/Users/Asus/Desktop/py/demo/Python_demo/demo_asyncio/demo2.py:11> result=None>
print(isinstance(task, asyncio.Future)) # True
loop.close()