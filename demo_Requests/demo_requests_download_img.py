import requests
from contextlib import closing

def download_img():
    url = 'http://www.chinacycc.com/data/attachment/forum/201705/25/210107ye3b0v3yqu2uxxmq.jpg'
    #   伪造请求头，模拟为浏览器
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    #   为了下载图片，只能以流的方式打开图片
    response = requests.get(url=url,headers=headers,stream=True)
    #   contextlib是上下文管理器，用来关闭流，避免资源浪费
    with closing(requests.get(url=url,headers=headers,stream=True)) as response:
        with open(r'C:\users\administrator\desktop\1.jpg','wb') as f:
            #   每128写入一次
            for i in response.iter_content(128):
                f.write(i)

if __name__ == '__main__':
    download_img()
