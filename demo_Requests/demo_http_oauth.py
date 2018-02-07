import requests

BASE_URL = 'https://api.github.com'

def construct_url(end_point):
    return '/'.join([BASE_URL,end_point])

def basic_oauth():
    headers = {'token':'7f18a2ae9de5c725d5375eee7d3deb5b41ab77a5'}
    response = requests.get(construct_url('user/emails'),headers=headers)
    print(response.text)
    print(response.request.headers)

if __name__ == '__main__':
    basic_oauth()