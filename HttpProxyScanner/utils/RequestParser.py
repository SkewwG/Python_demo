# coding:utf-8
import re

class RequestParserClass(object):

    def __init__(self, f):
        self.flow = f
        self.requestDict = {}
        self.request_id = None
        self.request_url = None
        self.request_method = None
        self.request_post_data = None
    def parser(self):
        print(dir(self.flow.request))
        '''
        flow.requests 的方法：
        ['__abstractmethods__', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', 
        '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
        '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_abc_cache', 
        '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', '_get_content_type_charset', 
        '_get_cookies', '_get_multipart_form', '_get_query', '_get_urlencoded_form', '_guess_encoding', 
        '_parse_host_header', '_set_cookies', '_set_multipart_form', '_set_query', '_set_urlencoded_form', 
        'anticache', 'anticomp', 'body', 'constrain_encoding', 'content', 'cookies', 'copy', 'data', 'decode', 
        'encode', 'first_line_format', 'from_state', 'get_content', 'get_state', 'get_text', 'headers', 'host', 
        'http_version', 'is_replay', 'method', 'multipart_form', 'path', 'path_components', 'port', 'pretty_host', 
        'pretty_url', 'query', 'raw_content', 'replace', 'scheme', 'set_content', 'set_state', 'set_text', 'stickyauth', 
        'stickycookie', 'text', 'timestamp_end', 'timestamp_start', 'url', 'urlencoded_form', 'wrap']
        '''
        # print('self.flow.request.headers : {}'.format(self.flow.request.headers))
        getheaders = re.findall(r'(.*?)\:.(.*?)\r\n', str(self.flow.request.headers), re.S)
        #print('getheaders : {}'.format(getheaders))
        for k, v in getheaders:
            self.requestDict[k] = v

        self.request_id = self.flow.id
        self.request_url = self.flow.request.url
        self.request_method = self.flow.request.method
        self.request_post_data = self.flow.request.raw_content