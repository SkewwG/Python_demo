import redis
r = redis.Redis(host='127.0.0.1',port=6379)
r.set('age','10')
r.decr('age','8')
print(r.get('age'))
r.decr('nnn','7')
print(r.get('nnn'))