import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def hello(self):
        return 'hello,wolrd!'

conf = {'global': {'server.socket_port': 8082,
'server.socket_host': '127.0.0.1'}}
cherrypy.config.update(conf)
cherrypy.quickstart(HelloWorld())