from bs4 import BeautifulSoup
'''
#1、格式化输出
print(soup.prettify())
'''
'''
#2、标签
print(soup.html.body.p.b)       #<b>The Dormouse's story</b>
print(soup.b)                   #<b>The Dormouse's story</b>

print(soup.name)                #[document]
print(soup.p.name)              #p
print(soup.p.attrs)             #{'class': ['title'], 'name': 'dromouse'}

print(soup.p.attrs['class'])    #['title']
'''
'''
#3、标签的内容
print(soup.b.string)                    #The Dormouse's story
'''
'''
#4、Comment对象是有注释符
print(soup.a)                               #<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
print(soup.a.string)                        #Elsie
print(type(soup.a.string))                  #<class 'bs4.element.Comment'>
print(type(soup.p.string))                  #<class 'bs4.element.NavigableString'>
'''

'''
#5、1直接子节点
#.contents
print(soup.head.contents)                   #[<title>The Dormouse's story</title>]
print(soup.head.contents[0])                #<title>The Dormouse's story</title>
print(soup.body)
print(soup.body.contents)

#.children
for child in soup.body.children:
    print(child,end='')

#.descendants
for child in soup.descendants:
    print(child,end='')
'''

'''
#6 .string
print(soup.head.string)
print(soup.title.string)
'''

'''
#7、多个内容
for string in soup.strings:
    print(string,end='')
print('-'*50)
for string in soup.stripped_strings:
    print(string,end='')
'''

'''
print(soup.find_all('p',class_='sister',id=re.compile('^link'),href='http://example.com/elsie'))
'''

import re
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html,'html5lib')
