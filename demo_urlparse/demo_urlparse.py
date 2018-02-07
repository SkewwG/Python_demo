from urllib.parse import urlparse

link1 = r'http://www.miibeian.gov.cn/sszx1.asp?id=31&a=1&b=callback'
link2 = r'www.miibeian.gov.cn/sszx1.asp?id=31'
link3 = r'miibeian.gov.cn/sszx1.asp?id=31'
link4 = r'sszx1.asp?id=31'
link5 = r'sszx1.asp'
ret1 = urlparse(link1)
ret2 = urlparse(link2)
ret3 = urlparse(link3)
ret4 = urlparse(link4)
ret5 = urlparse(link5)
print(ret1)
print(link1.replace(ret1.query,''))
print(ret2)
print(ret3)
print(ret4)
print(ret5)
links = [link1,link2,link3,link4,link5]
# 动态链接爬行中过滤掉带有http或者www的链接。
for link in links:
    ret = urlparse(link)
    if ret.scheme:
        link_ret = link
    elif ret.path.split('.')[0] == 'www':
        link_ret = 'http://' + link
    else:
        link_ret = 'http://www.' + link
        #print(link)
    print(link_ret)