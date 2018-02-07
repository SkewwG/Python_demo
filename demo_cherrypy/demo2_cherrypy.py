import cherrypy

class HelloWorld:
    def hello2(self):
        return "hello ske2."
    hello2.exposed = True               #暴露此函数才能被url get到
cherrypy.quickstart(HelloWorld())