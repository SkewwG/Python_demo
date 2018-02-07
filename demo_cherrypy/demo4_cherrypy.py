'''
hello方法，注意后面的firstname和lastname两个参数，这个两个参数对应到浏览器的参数。
这个hello方法对应到http://localhost:8080/hello/Jeffery/Sun
或者http://localhost:8080/hello?firstname=Jeffery&lastname=Sun。
注意，当把参数直接作为地址的一部分传递时(第一个URL)，CherryPy会根据 “/”分开URL赋值给方法参数。
但是如果用浏览器参数形式传递(第二个URL)，浏览器参数名称必须能和方法参数名对应上。

default方法，default方法有特殊的含义，它本身除了一般的方法的意思之外，
还用于匹配与它参数个数一致的请求，一般可以用来作为非法URL的错误处理。
上面的default方法可以对应到这个URL：http://localhost:8080/default/2007/10/20/lijianwei，
参数year对应到2007，month对应到10，day对应到20，aa对应到lijianwei。
但是它也对应到如下的几个URL：http://localhost:8080/aaa/bbb/ccc/dddd和http://localhost:8080/111/222/333/444等，
也就是说虽然这两个URL对应不到任何的一个Python的方法，但是由于分开后的参数个数能与default方法对应上，
所以还是会匹配到default方法，这就是default方法的一个特殊作用。
一个正常的请求到达后，首先进行正常的匹配，看能否找到一个合适的方法，
如果没有，那么就会去和default匹配，看参数个数是否一样，如果还是不匹配就会抛出404错误。

'''
import cherrypy

class HelloWorld:
    @cherrypy.expose                                    #暴露此函数才能被url get到
    def hello(self,firstName,lastName):
        return "hello"+firstName+lastName               #http://127.0.0.1:8080/hello/ske/baige  http://127.0.0.1:8080/hello?firstName=ske&lastName=baige

    @cherrypy.expose
    def default(self,year,month,day,name):
        return 'error'                                  #http://127.0.0.1:8080/1111/222222/3333333/44444444

cherrypy.quickstart(HelloWorld())