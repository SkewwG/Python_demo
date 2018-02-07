import gevent
import socket
import time

start_time = time.time()
urls = ['www.baidu.com','www.qq.com','www.lrzdjx.com','www.ske.vc']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]        #gevent.spawn(方法，参数)
gevent.joinall(jobs, timeout=5)                                         #gevent.joinall(列表,timeout=?)
end_time = time.time()
times = end_time - start_time

print([job.value for job in jobs])                                      #.value获取返回的值
print('cost time:',times)