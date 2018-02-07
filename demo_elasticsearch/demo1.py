from elasticsearch import Elasticsearch
from datetime import datetime

# 连接Elasticsearch
es = Elasticsearch()

# 创建索引，一旦执行之后，就得注释掉，因为当索引存在，就无法继续运行下去
# es.indices.create(index='my-index')


# 添加数据
es.index(index="my-index",doc_type="test-type",id=2,body={"any":"data01","timestamp":datetime.now()})

# get获取数据
res = es.get(index="my-index", doc_type="test-type", id=2)
print('get : {}'.format(res))
print('_source : {}'.format(res['_source']))

# search查询数据
res = es.search(index="my-index", body={"query":{"match_all":{}}})
print('search : {}'.format(res))
for hit in res['hits']['hits']:
    print(hit["_source"])

res = es.search(index="my-index", body={'query':{'match':{'any':'data'}}}) #获取any=data的所有值
print(res)