from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)      # 连接客户端
db = conn.skedb                             # 连接数据库
my_set = db.skeCollection                   # 选择集合
my_set.insert({'name':'ske'})               # 插入数据