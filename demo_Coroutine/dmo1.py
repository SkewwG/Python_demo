def consumer():
    r = 'start'
    a = ''
    while True:
        n = yield a
        print('r : {}'.format(r))
        print('a : {}'.format(a))
        print('n : {}'.format(n))
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)