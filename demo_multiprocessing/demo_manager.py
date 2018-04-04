from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support  #server启动报错，提示需要引用此包
import random,time,queue

#发送任务的队列
task_queue = queue.Queue()
#接收结果的队列
result_queue = queue.Queue()

#从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass
#win7 64 貌似不支持callable下调用匿名函数lambda，这里封装一下
def return_task_queue():
    global task_queue
    return task_queue
def return_result_queue():
    global result_queue
    return result_queue

def test():
    #把两个Queue注册到网络上，callable参数关联了Queue对象
    #QueueManager.register('get_task_queue',callable=lambda:task_queue)
    #QueueManager.register('get_result_queue',callable=lambda:result_queue)
    QueueManager.register('get_task_queue111',callable=return_task_queue)
    QueueManager.register('get_result_queue111',callable=return_result_queue)
    #绑定端口5000，设置验证码‘abc’
    manager = QueueManager(address=('0.0.0.0',5000),authkey=b'abc')#这里必须加上本地默认ip地址127.0.0.1
    #启动Queue
    manager.start()
    #server = manager.get_server()
    #server.serve_forever()
    print('start server master')
    #获得通过网络访问的Queue对象
    print(dir(manager))
    task = manager.get_task_queue111()
    result = manager.get_result_queue111()
    #放几个任务进去
    for i in range(10):
        n = random.randint(0,10000)
        print('put task %d...' % n)
        task.put(n)
    #从result队列读取结果
    print('try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('result:%s' % r)

    #关闭
    manager.shutdown()
    print('master exit')

if __name__ == '__main__':
    freeze_support()
    test()