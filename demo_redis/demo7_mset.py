import redis
r = redis.Redis(host='127.0.0.1',port=6379)
r.mset(name='tom',age='18',school='china')
print(r.get('name'))
print(r.get('age'))
print(r.get('school'))