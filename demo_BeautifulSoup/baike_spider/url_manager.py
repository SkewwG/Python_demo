#-*- coding:utf-8 -*-

class UrlManager():

    def __init__(self):
        self.new_urls = set()                                           # 待爬取的url集合
        self.old_urls = set()                                           # 已爬取的url集合

    def add_new_url(self,url):
        '''
        将root_url存入到new_urls里
        :param url:
        :return:
        '''
        if url is None:
            return None
        if url not in self.new_urls and url not in self.old_urls:       # 如果该url既不在待爬取的url集合里，也不在已爬取的url集合里，则添加到待爬取的url集合里
            self.new_urls.add(url)


    def add_new_urls(self, urls):
        '''
        将爬取的某个url后获得的新的urls存入待爬取的url集合里
        :param urls: 爬取的某个url后获得的新的urls
        :return: 存入待爬取的url集合里
        '''
        if urls is None or len(urls) == 0:
            return
        for url in urls:                                                # 将爬取到的url添加到待爬取的url集合里
            self.new_urls.add(url)

    def has_new_url(self):
        return len(self.new_urls) != 0                                  # 如果待爬取的url集合不为空，即说明还有可以爬取的url，返回True

    def get_new_url(self):
        new_url = self.new_urls.pop()                                   # 待爬取得到url集合里取出一条url爬取
        self.old_urls.add(new_url)                                      # 已爬取的url集合里添加刚取出的url
        return new_url                                                  # 返回取出的url

