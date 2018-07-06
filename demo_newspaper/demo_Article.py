# article的使用方法
from newspaper import Article

# print(help(Article))
url = r'https://new.qq.com/omn/20180705/20180705A0T4T4.html'
article = Article(url)      # an online news article page

article.download()      # 下载文章

html = article.html     # 网页源代码
# print(html)

article.parse()         # 文章解析

authors = article.authors       # 文章作者
# print(authors)

publish_date = article.publish_date     # 文章发布时间
# print(publish_date)

text = article.text             # 文章内容
# print(text)

top_image = article.top_image       # 第一张图片
# print(top_image)

movies = article.movies         # 视频链接
# print(movies)

title = article.title           # 文章标题
print(title)
'''
class Article(builtins.object)
 |  Article objects abstract an online news article page
 |  
 |  Methods defined here:
 |  
 |  __init__(self, url, title='', source_url='', config=None, **kwargs)
 |      The **kwargs argument may be filled with config values, which
 |      is added into the config object
 |  download(self, input_html=None, title=None, recursion_counter=0)
 |      Downloads the link's HTML content, don't use if you are batch async
 |      downloading articles
 |      
 |      recursion_counter (currently 1) stops refreshes that are potentially
 |      infinite
'''