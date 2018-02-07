# A记录（实现A记录查询方法源码）
import dns.resolver

domain = 'ske.vc'
A = dns.resolver.query(domain,'A')
print(A.response.answer)
for i in A.response.answer:
    print(i)
    for j in i.items:
        print(j.address)                    #103.200.116.16