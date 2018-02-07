# NS记录（实现NS记录查询方法源码）：
import dns.resolver

domain = r'baidu.com'
ns = dns.resolver.query(domain,'NS')
for i in ns.response.answer:
    for j in i.items:
        print(j.to_text())