import cherrypy

class HelloWorld:
    @cherrypy.expose            #暴露此函数才能被url get到
    def hello(self):
        return 'hello,wolrd!'
cherrypy.quickstart(HelloWorld())