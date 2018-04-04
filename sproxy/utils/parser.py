# from __future__ import absolute_import

class ResponseParser(object):
    """docstring for ResponseParser"""

    def __init__(self, f):
        super(ResponseParser, self).__init__()
        self.flow = f

    def parser_data(self):
        result = dict()
        result['url'] = self.flow.request.url
        result['path'] = '/{}'.format('/'.join(self.flow.request.path_components))
        result['host'] = self.flow.request.host
        result['port'] = self.flow.request.port
        result['scheme'] = self.flow.request.scheme
        result['method'] = self.flow.request.method
        result['status_code'] = self.flow.response.status_code
        result['content_length'] = int(self.flow.response.headers.get('Content-Length', 0))
        result['request_header'] = self.parser_header(self.flow.request.headers)
        result['request_content'] = self.flow.request.content
        return result

    @staticmethod
    def parser_multipart(content):
        if isinstance(content, str):
            res = re.findall(r'name=\"(\w+)\"\r\n\r\n(\w+)', content)
            if res:
                return "&".join([k + '=' + v for k, v in res])
            else:
                return ""
        else:
            return ""

    @staticmethod
    def parser_header(header):
        headers = {}
        for key, value in header.items():
            headers[key] = value
        return headers

    @staticmethod
    def decode_response_text(content):
        for _ in ['UTF-8', 'GB2312', 'GBK', 'iso-8859-1', 'big5']:
            try:
                return content.decode(_)
            except:
                continue
        return content