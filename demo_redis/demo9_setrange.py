import redis
r = redis.Redis(host='127.0.0.1',port=6379)
r.set('name','tomnameeeeeeeeee')
r.setrange('name',0,'python')
print(r.get('name'))