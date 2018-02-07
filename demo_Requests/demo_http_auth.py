import requests

BASE_URL = 'https://api.github.com'

def construct_url(end_point):
    return '/'.join([BASE_URL,end_point])

def basic_auth():
    response = requests.get(construct_url('user'),auth=('skeletonbg','Ske123!@#'))
    print(response.text)
    print(response.request.headers)

if __name__ == '__main__':
    basic_auth()