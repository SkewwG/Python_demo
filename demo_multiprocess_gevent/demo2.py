import gevent

import requests

def func(url):
    res = requests.get(url)
    code = res.status_code
    print(code)

urls = ['http://www.baidu.com', 'http://blog.csdn.net/qq_33733970/article/details/77983848', 'http://python.jobbole.com/87310/']
jobs = [gevent.spawn(func, url) for url in urls]
gevent.joinall(jobs)