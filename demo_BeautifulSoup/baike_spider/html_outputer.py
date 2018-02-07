# coding:utf-8

class HtmlOutputer():
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        import chardet
        with open('output.html', 'w',encoding='utf-8') as f:                    #不能是'wb'.只能是w       而且必须得编码encoding="utf-8"
            f.write('<html>')
            f.write('<body')
            for data in self.datas:
                f.write('<tr>')
                f.write('<br>')
                f.write('<td>%s</td>' % data['url'])
                f.write('<td>%s</td>' % data['title'])                          #此处就无需编码.encode()
                f.write('<td>%s</td>' % data['summary'])
                f.write('</br>')
                f.write('</tr>')
            f.write('</body')
            f.write('</html>')