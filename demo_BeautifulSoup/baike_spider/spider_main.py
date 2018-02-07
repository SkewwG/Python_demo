#-*- coding:utf-8 -*-

from demo_BeautifulSoup.baike_spider import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain():
    def __init__(self):
        self.urls = url_manager.UrlManager()                                    # 管理器对象
        self.downloader = html_downloader.HtmlDownloader()                      # 下载器对象
        self.parser = html_parser.HtmlParser()                                  # 解析器对象
        self.outputer = html_outputer.HtmlOutputer()                            # 输出器对象

    def craw(self, root_url):
        count = 1                                                               # 记录爬取的是第几条url
        self.urls.add_new_url(root_url)                                         # add_new_url是添加一条url，将入口url添加到urls管理器
        while self.urls.has_new_url():                                          # 如果urls管理器内有新的url则开始爬行新的url
            try:                                                                # 异常
                new_url = self.urls.get_new_url()                               # 从urls管理器内获取新的url进行爬取
                print('craw {0} : {1}'.format(count, new_url))                   # 打印爬取的是第几条url
                html_content = self.downloader.download(new_url)                # 下载器
                new_urls, new_data = self.parser.parse(new_url, html_content)     # 解析器，得到新的urls和数据data
                self.urls.add_new_urls(new_urls)                                # 把爬取到的新的url添加到urls管理器内
                self.outputer.collect_data(new_data)
                if count == 1:                                                # 爬行达到1000就停止
                    break

                count += 1
            except Exception as e:
                print('craw failed! error : {0}'.format(e))
        self.outputer.output_html()                                                  # 将爬取的内容打印出来

if __name__ == '__main__':
    root_url = r'http://baike.baidu.com/link?url=l7cApbfEY5W5cnryTc5Q274FIxbafZnWhSYcVSk6hTgD1GwjTHWbEpeUKZiPMtDpKPTn9vRvH5ntEYrqBF275K'       #爬取入口
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)                                                                 #启动爬虫