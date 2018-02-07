import requests
import json
from requests import Session,Request

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def sesson_requests():
    s = Session()                                                                                        #创建一个会话
    headers = {'User-Agent':'skeleton'}                                                                  #可以伪造请求头
    req = Request('GET', build_uri('user/emails'),headers=headers,auth=('skeletonbg','Ske123!@#'))       #因为是底层，所以用Request
    prepared = req.prepare()                                                                             #准备
    response = s.send(prepared,timeout=5)                                                                #发送
    print(better_print(response.text))
    print(response.request.headers)

if __name__ == '__main__':
    sesson_requests()