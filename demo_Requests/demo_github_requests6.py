import json
import requests
from requests import exceptions


URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def timeout_requests():
    try:
        response = requests.get(build_uri('user/emails'),timeout=10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print(str(e))
    except exceptions.HTTPError as e:
        print(str(e))


if __name__ == '__main__':
    timeout_requests()