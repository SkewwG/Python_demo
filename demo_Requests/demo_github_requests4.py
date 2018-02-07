#requests.patch的json
import json
import requests

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    return  json.dumps(json.loads(json_str),indent=4)

def json_requests():
    before_response = requests.get(build_uri('user'),auth=('skeletonbg','Ske123!@#'))
    after_response = requests.patch(build_uri('user'),auth=('skeletonbg','Ske123!@#'),json={'name':'ske','email':'1473605323@qq.com'})
    print(better_print(before_response.text))
    print(better_print(after_response.text))
    print(after_response.request.headers)
    print(after_response.request.body)
    print(after_response.status_code)

if __name__ == '__main__':
    json_requests()