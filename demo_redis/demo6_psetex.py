'''
psetex(name,time_ms,value)
# 设置值
# 参数：
# time_ms，过期时间（数字毫秒 或 timedelta对象）
'''
import redis
import time
r = redis.Redis(host='127.0.0.1',port=6379)
r.psetex('name','1','test')
print(r.get('name'))
time.sleep(0.1)
print(r.get('name'))