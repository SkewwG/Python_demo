from lxml import etree
import requests

url = r'http://www.futures.pingan.com'
response = requests.get(url=url)
parser = etree.HTML(response.content)
print(parser)