'''
这里有一个hello和index方法，hello方法对应的URL是http://localhost:8080/hello。
index方法对应的URL是http://localhost:8080/index，
但是index这个方法也对应到http://localhost:8080这个地址，
相当于一个默认的方法，类似于IIS中设置的index.html、default.html等页面。
'''
import cherrypy

class HelloWorld:
    @cherrypy.expose                            #暴露此函数才能被url get到
    def hello3(self):
        return "hello sek."

    @cherrypy.expose
    def index(self):
        return "hello welcome index."

cherrypy.quickstart(HelloWorld())