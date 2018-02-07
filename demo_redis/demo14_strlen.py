import redis
r = redis.Redis(host='127.0.0.1',port=6379)
r.set('name','python')
print(r.strlen('name'))