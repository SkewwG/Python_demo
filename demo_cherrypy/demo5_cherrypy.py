'''

    如果请求为http://localhost:8080。直接对应到Man类的index方法，所以输出是:"i’m man”。
    如果请求为http://localhost:8080/sayhello。对应到Man类的sayhello方法，所以输出是:"hello,i’m man”。
    如果请求为http://localhost:8080/wife。对应到Man类的wife变量，因此对应到Wife类的index方法，输出是:"i’m wife”。
    如果请求为http://localhost:8080/wife/sayhello。对应到Man类的wife变量的sayhello方法，输出是:"hello,i’m wife”。
    brother和wife类似。

'''
import cherrypy

class Wife:
    @cherrypy.expose                            #暴露此函数才能被url get到
    def index(self):
        return 'I\'m Wife'

    @cherrypy.expose
    def sayHello(self):
        return 'hello Wife'


class Bro:
    @cherrypy.expose
    def index(self):
        return 'I\'m Bro'

    @cherrypy.expose
    def sayHello(self):
        return 'hello Bro'

class Man:
    wife = Wife()
    bro = Bro()
    @cherrypy.expose
    def index(self):
        return 'I\'m man'

    @cherrypy.expose
    def sayHello(self):
        return 'hello Man'

cherrypy.quickstart(Man())

'''
http://127.0.0.1:8080/
http://127.0.0.1:8080/Man
http://127.0.0.1:8080/Man/sayHello

http://127.0.0.1:8080/wife/
http://127.0.0.1:8080/wife/sayHello

http://127.0.0.1:8080/bro/
http://127.0.0.1:8080/bro/sayHello
'''