import asyncio
import time
import threading
import functools

@asyncio.coroutine
def do_some_work():
    print(threading.current_thread(), time.time())
    r = yield from asyncio.sleep(1)
    print(threading.current_thread(), time.time())
    return 'do_some_work Done'

# 回调, 传递多参数
def callback(t, future):
    print(future)       # <Task finished coro=<do_some_work() done, defined at C:/Users/Asus/Desktop/py/demo/Python_demo/demo_asyncio/test.py:5> result='do_some_work Done'>
    print(dir(future))
    print('Callback : {} {}'.format(t, future.result()))          # Callback : 2 do_some_work Done

loop = asyncio.get_event_loop()
task = loop.create_task(do_some_work())
'''
task = loop.create_task(do_some_work())
task            # <Task pending coro=<do_some_work() running at C:/Users/Asus/Desktop/py/demo/Python_demo/demo_asyncio/test.py:5>>      pending:在等待…期间
type(task)      # <class 'asyncio.tasks.Task'> create_task创建一个task对象
dir(task)
['__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
'__weakref__', '_all_tasks', '_blocking', '_callbacks', '_copy_state', '_coro', '_current_tasks', '_exception', 
'_format_callbacks', '_fut_waiter', '_log_destroy_pending', '_log_traceback', '_loop', '_must_cancel', '_repr_info', 
'_result', '_schedule_callbacks', '_set_result_unless_cancelled', '_source_traceback', '_state', '_step', '_tb_logger', 
'_wakeup', 'add_done_callback', 'all_tasks', 'cancel', 'cancelled', 'current_task', 'done', 'exception', 'get_stack', 
'print_stack', 'remove_done_callback', 'result', 'set_exception', 'set_result']
'''
task.add_done_callback(functools.partial(callback, 2))  # task和callback回调里的future对象，实际上是同一个对象
loop.run_until_complete(task)       # 此时才是真正的开始执行do_some_work函数里的代码
loop.close()