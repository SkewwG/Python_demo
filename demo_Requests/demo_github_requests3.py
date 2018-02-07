#requests.ge的params用法
import json
import requests

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    return  json.dumps(json.loads(json_str),indent=4)

def params_requests():
    response = requests.get(build_uri('users'),params={'since':11})
    print(better_print(response.text))
    print(response.headers)
    print(response.url)

if __name__ == '__main__':
    params_requests()