#获取emails
import json
import requests

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    return  json.dumps(json.loads(json_str),indent=4)

def request_method():
    #获取emails
    response = requests.get(build_uri('user/emails'),auth=('skeletonbg','Ske123!@#'))
    print(response.text)
    print(better_print(response.text))

if __name__ == '__main__':
    request_method()