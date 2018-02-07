#requests.patch的json
import json
import requests

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    return  json.dumps(json.loads(json_str),indent=4)

def json_requests():
    response = requests.post(build_uri('user/emails'),auth=('skeletonbg','Ske123!@#'),json=['44610652511@qq.com'])
    print(better_print(response.text))

if __name__ == '__main__':
    json_requests()