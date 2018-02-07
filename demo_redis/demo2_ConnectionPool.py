'''连接池
redis使用connection pool来管理对一个redis server 的所有连接，避免每次建立，释放连接的开销，
默认，每个Redis实例都会维护一个自己的连接池。
可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池。
'''
import redis
pool = redis.ConnectionPool(host='127.0.0.1',port=6379)
r = redis.Redis(connection_pool=pool)
r.set('age','16')
print(r.get('name'))
