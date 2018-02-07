import redis
r = redis.Redis(host='127.0.0.1',port=6379)
r.set('age','2')
r.incr('age','5')
print(r.get('age'))
r.incr('num','10')
print(r.get('num'))