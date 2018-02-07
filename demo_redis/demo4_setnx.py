'''
setnx(name,value)
设置值，只有name不存在时，执行设置操作（添加）
'''
import redis
r = redis.Redis(host='127.0.0.1',port=6379)
r.setnx('name','tom')
print(r.get('name'))