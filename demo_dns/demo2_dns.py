#-*- coding:utf-8 -*-
# MX记录（实现MX记录查询方法源码）：

import dns.resolver
domain = r'163.com'
MX = dns.resolver.query(domain,'MX')
for i in MX:
    print('MX preference =', i.preference, 'mail exchanger =', i.exchange)