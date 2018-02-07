import urllib.request

url = "http://www.sxgt.net/"
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)

info = response.info()
add = response.geturl()
code = response.getcode()
body = response.read().decode('utf-8')

print(">>>info:↓\n{0}".format(info))
print(">>>add:↓\n{0}".format(add))
print(">>>code:↓\n{0}".format(code))
print(">>>body:↓\n{0}".format(body))
