import redis
r = redis.Redis(host='127.0.0.1',port=6379)
r.set('name','python')
print(r.get('name'))
r.setbit('name','6','1')
print(r.get('name'))