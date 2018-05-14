d = {}
d['1'] = 'a'
d['4'] = 'aaaa'
d['2'] = 'aa'
d['3'] = 'aaa'

ret = sorted(d.items(), key=lambda x:x[0])
print(ret)
