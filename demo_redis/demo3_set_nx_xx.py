'''
set(name, value, ex=None, px=None, nx=False, xx=False)
在Redis中设置值，默认，不存在则创建，存在则修改
参数：
ex，过期时间（秒）
px，过期时间（毫秒）
nx，如果设置为True，则只有name不存在时，当前set操作才执行
xx，如果设置为True，则只有name存在时，当前set操作才执行
'''
import redis
r = redis.Redis(host='127.0.0.1',port=6379)
r.set('age0','22',nx=True)
print(r.get('age0'))

r.set('age1','22',xx=True)
print(r.get('age1'))