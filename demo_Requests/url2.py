import urllib.request
import urllib.parse

def url_1(url1):
    '简单的urllib实例'

    req = urllib.request.Request(url1)
    response = urllib.request.urlopen(req)

    info = response.info()
    add = response.geturl()
    code = response.getcode()
    body = response.read().decode('utf-8')

    print(">>>info:↓\n{0}".format(info))
    print(">>>add:↓\n{0}".format(add))
    print(">>>code:↓\n{0}".format(code))
    print(">>>body:↓\n{0}".format(body))

def url_2(url2):
    '构造请求参数'
    data = {'RecordId':'280','catalogID':'69','type':'dL'}
    params = urllib.parse.urlencode(data)
    print('>>>params:↓\n{0}'.format(params))
    '连接域名和参数构造带参数的url'
    realUrl = '?'.join([url2,params])
    print('>>>url:↓\n{0}'.format(realUrl))
    '打印带参数的url的信息'
    url_1(realUrl)

if __name__ == '__main__':

    url2 = 'http://www.sxgt.net/NewDetail.aspx'
    url_2(url2)
