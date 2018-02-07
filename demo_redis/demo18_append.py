import redis
r = redis.Redis(host='127.0.0.1',port=6379)
r.set('name','python')
r.append('name','3.4')
print(r.get('name'))