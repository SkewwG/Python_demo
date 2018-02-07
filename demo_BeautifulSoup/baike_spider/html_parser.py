#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re
import urllib


class HtmlParser():                                                                                 #解析器

    def __get__new__urls(self,page_url,soup):
        new_urls = set()                                                                            # 获取到的新的url集合，设置成set集合是为了去重
        # /view/123.htm
        links = soup.find_all('a',href=re.compile(r'/view/\d+\.htm'))                               # 正则匹配
        for link in links:
            new_url = link['href']                                                                  # 获取href属性的值
            new_full_url = urllib.parse.urljoin(page_url,new_url)                                   # 拼接url
            '''
            >>> url1 = 'http://www.baidu.com'
            >>> url2 = 'a/2.hml'
            >>> url = urllib.parse.urljoin(url1,url2)
            url>>>'http://www.baidu.com/a/2.hml'
            '''
            new_urls.add(new_full_url)                                                              # 放到集合里
        return new_urls

    def __get__new__data(self,page_url,soup):
        res_data = {}
        # url
        res_data['url'] = page_url                                                                  # 爬行的当前url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')                  # 获取爬行页面的标题
        res_data['title'] = title_node.get_text()
        # <div class="lemma-summary">
        summary_node = soup.find('div',class_='lemma-summary')                                      # 获取爬行页面的summary
        res_data['summary'] = summary_node.get_text()
        return res_data

    def parse(self,page_url,html_content):
        '''
        将爬取到的第n条url和该url的源代码解析。返回源代码里的新的url和data数据
        :param page_url: 爬取到的第n条url
        :param html_content: url的源代码
        :return: 返回源代码里的新的url和data数据
        '''
        if page_url is None and html_content is None:
            return
        soup = BeautifulSoup(html_content,'html.parser')
        new_urls = self.__get__new__urls(page_url,soup)                                             # 获取爬行到的新的urls，传递page_url是为了拼接完整的url
        new_data = self.__get__new__data(page_url,soup)                                             # 获取爬行的该页面的数据
        return new_urls,new_data