#对socket标准库打上猴子补丁，此后socket标准库中的类和方法都会被替换成非阻塞式的，所有其他的代码都不用修改，这样协程的效率就真正体现出来了。
from gevent import monkey
monkey.patch_all()
import socket
import gevent
import time

start_time = time.time()
urls = ['www.baidu.com','www.qq.com','www.lrzdjx.com','www.ske.vc']
jobs = [gevent.spawn(socket.gethostbyname,url) for url in urls]
gevent.joinall(jobs,timeout=5)
end_time = time.time()
times = end_time - start_time
print([job.value for job in jobs])
print('cost time:',times)