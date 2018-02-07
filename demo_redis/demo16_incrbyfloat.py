import redis
r = redis.Redis(host='127.0.0.1',port=6379)
r.set('age','1')
r.incrbyfloat('age','2.0')
print(r.get('age'))