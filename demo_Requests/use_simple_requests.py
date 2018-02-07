import requests

def use_simple_requests(url_1):
    '简单的requests实例'

    response = requests.get(url_1)
    head = response.headers
    add = response.url
    state = response.status_code
    body = response.text

    print(">>>info:↓\n{0}".format(head))
    print(">>>add:↓\n{0}".format(add))
    print(">>>code:↓\n{0}".format(state))
    #print(">>>body:↓\n{0}".format(body))
    print("-"*100)

def use_simple_requeses_2(url_2):
    '构造请求参数'
    data = {'RecordId':'280','catalogID':'69','type':'dL'}
    '连接域名和参数构造带参数的url'
    response = requests.get(url_2,data)

    add = response.url
    print('>>>url:↓\n{0}'.format(add))
    '打印带参数的url的信息'
    use_simple_requests(add)

if __name__ == '__main__':
    url_1 = 'http://www.sxgt.net'
    use_simple_requests(url_1)


    url_2 = 'http://www.sxgt.net/NewDetail.aspx'
    use_simple_requeses_2(url_2)
