# coding:utf-8
from mitmproxy import flow, proxy, options, controller
from pprint import pprint
from mitmproxy.proxy.server import ProxyServer
from utils.RequestParser import RequestParserClass

class ProxyClass(flow.FlowMaster):

    def __init__(self, opts, server, state):
        super(ProxyClass, self).__init__(opts, server, state)
        self.static_ext = [
            'js', 'css', 'png', 'jpg', 'gif', 'jpeg',
            'bmp', 'ico'
            ]
        self.filter_url = [
            'mozilla.com', 'bing.com', 'baidu.com/',
            'jd.com/', 'wpad.dat', 'firefox.com/', 't00ls.net'
        ]

    def run(self):
        try:
            pprint("Start")
            flow.FlowMaster.run(self)
        except KeyboardInterrupt as e:
            pprint("shutdown")
            self.shutdown()

    def filter_extension(self, flow):
        _ = flow.request.path_components
        #print('[_] = {} '.format(_))
        if _ == ():
            return False
        url_ext = _[0] if len(_) == 1 else _[-1]
        url_ext = url_ext.split('.')
        url = flow.request.url

        # filter the static file
        for ft in self.static_ext:
            # print url_ext
            if ft in url_ext:
                return True

        # filter the url
        for u in self.filter_url:
            if u in url:
                return True

    @controller.handler
    def response(self, f):
        pass

    @controller.handler
    def request(self, f):
        # print('f : {}'.format(f))
        '''
        f : <HTTPFlow
            request = Request(GET detectportal.firefox.com:80/success.txt)
            client_conn = <ClientConnection: 127.0.0.1:60158>
            server_conn = <ServerConnection: a1.cnblogs.com:80>>
        '''
        rp = RequestParserClass(f)
        '''
        rp : <utils.RequestParser.RequestParserClass object at 0x074FD870>
        '''
        #print('rp : {}'.format(rp))
        rp.parser()
        # print f.request.path_components
        if not self.filter_extension(rp.flow):
            #print("[Request ID] {}".format(rp.request_id))
            #print("[Request URL][Method {}] {}".format(rp.request_method, rp.request_url))
            if rp.request_method == 'POST':
                pass
                #print("POST DATA: {}".format(rp.request_post_data))

    @controller.handler
    def error(self, f):
        pass

    @controller.handler
    def log(self, l):
        pass

def start_server(proxy_port, proxy_mode):
    port = int(proxy_port) if proxy_port else 8090
    mode = proxy_mode if proxy_mode else 'regular'

    if proxy_mode == 'http':
        mode = 'regular'

    opts = options.Options(
        listen_port=port,
        mode=mode,
        cadir="~/.mitmproxy/",
        )
    config = proxy.ProxyConfig(opts)
    state = flow.State()
    server = ProxyServer(config)
    m = ProxyClass(opts, server, state)
    m.run()

start_server('8090', 'http')