'''
 setex(name,value,time)
# 设置值
# 参数：
# time，过期时间（数字秒 或 timedelta对象）
'''

import redis
r = redis.Redis(host='127.0.0.1',port=6379)
r.setex('name','tom','1')
print(r.get('name'))
