
import dns.resolver

domain = r'www.baidu.com'
cname = dns.resolver.query(domain,'CNAME')
for i in cname.response.answer:
    for j in i.items:
        print(j.to_text())