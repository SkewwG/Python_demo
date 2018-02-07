# -*- coding: utf-8 -*-
import requests

def get_key_info(response, *args, **kwargs):
    """callback function"""
    print(response.headers['Content-Type'])

def main():
    """
    主程序

    """
    requests.get('http://www.baidu.com', hooks=dict(response=get_key_info))


if __name__ == '__main__':
    main()