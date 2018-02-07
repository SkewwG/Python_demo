from datetime import datetime
from elasticsearch import Elasticsearch
import elasticsearch.helpers
import random

es = Elasticsearch("localhost:9200")
package = []
for i in range(10):
    row = {
        "@timestamp":datetime.now().strftime( "%Y-%m-%dT%H:%M:%S.000+0800" ),
        "http_code" : "404",
        "count" : random.randint(1, 100)
    }
    package.append(row)

actions = [
    {
        '_op_type': 'index',
        '_index': "http_code",
        '_type': "error_code",
        '_source': d
    }
    for d in package
]

elasticsearch.helpers.bulk( es, actions)