#-*- coding:utf-8 -*-
import requests

class HtmlDownloader():
    '''
    网页下载器
    '''

    def download(self,url):
        '''
        返回url的源代码
        :param url:
        :return:
        '''
        if url is None:
            return None
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return response.content                            #一定要返回content而不是text   不然会乱码。需要的是content的bytes字节型