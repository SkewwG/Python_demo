from optparse import OptionParser
from urllib.parse import urlparse

if __name__ == '__main__':
    usage = r'usage : %prog demo_1'
    parse = OptionParser(usage=usage)
    parse.add_option('-k','--keywords',dest='keywords',type='string',help='search keywords.')
    parse.add_option('-p','--pages',dest='pages',type='int',help='the num of search results')
    options ,args = parse.parse_args()
    print('keywords : {0} type : {1}'.format(options.keywords,type(options.keywords)))
    print('pages : {0} type : {1}'.format(options.pages,type(options.pages)))