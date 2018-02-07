# 字典保持有序
from collections import OrderedDict
import json

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
print(d)                # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# 转换成json格式
j = json.dumps(d)
print(j)                # {"a": 1, "b": 2, "c": 3, "d": 4}