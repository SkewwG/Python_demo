import redis
r = redis.Redis(host='127.0.0.1',port=6379)
r.mset(n1=11,n2=21,n3=11)
r.bitop('AND','new_r','n1','n2','n3')
print(r.get('new_r'))