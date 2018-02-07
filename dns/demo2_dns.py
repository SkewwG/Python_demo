# MX记录（实现MX记录查询方法源码）：
import dns.resolver

domain = r'qq.com'
MX = dns.resolver.query(domain,'MX')
for i in MX:
    print('MX preference =', i.preference, 'mail exchanger =', str(i.exchange)[:-1])