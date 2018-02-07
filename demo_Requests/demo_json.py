import json
data1 = {'b':789,'c':456,'a':123}
d1 = json.dumps(data1,sort_keys=True,indent=4)
d1_type = type(d1)
data1_type = type(data1)
print('>>>d1={0}'.format(d1))
print('>>>d1_type{0}'.format(d1_type))
print('>>>data1{0}'.format(data1_type))

