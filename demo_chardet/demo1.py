import chardet
import requests

url1 = r'http://113.140.8.106:8080/'
url2 = r'http://115.231.58.130:8022/'
cont1 = requests.get(url1).content
cont2 = requests.get(url2).content
ret1 = chardet.detect(cont1)
ret2 = chardet.detect(cont2)
print(ret1)
print(ret2)