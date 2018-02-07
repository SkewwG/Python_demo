#爬取国外代理IP，并验证是否有效
from bs4 import BeautifulSoup
import requests
import random

#爬取所有代理IP和端口
def get_ip_list(ret):
    soup = BeautifulSoup(ret,'html.parser')
    ips = soup.find_all('tr')
    proxy_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        proxy_list.append('http://' + tds[0].string + ':' + tds[1].string)
    return proxy_list

#查询代理IP是否有效
def search_ip(headers,proxy_list):
    while True:
        try:
            #random.choice从一个列表里随机抽取一条数据
            proxy_ip = random.choice(proxy_list)
            proxies = {'http': proxy_ip}
            print('随机获取代理IP：', proxies)
            #该网址可以查询自身IP
            url = r'http://www.whatismyip.com.tw/'
            response = requests.get(url=url,headers=headers,proxies=proxies)
            code = response.status_code
            print('code : ',code)
            #打印IP
            ret = response.text
            soup = BeautifulSoup(ret, 'html.parser')
            ip = soup.find('b')
            print('search IP:', ip.text)
        except Exception as e:
            print('error : ',e)

if __name__ == '__main__':
    url = r'http://www.kuaidaili.com/free/outha/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
    response = requests.get(url=url,headers=headers)
    proxy_list = get_ip_list(response.text)
    search_ip(headers,proxy_list)