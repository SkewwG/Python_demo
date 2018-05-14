#协程,通过values获取返回值

import gevent
import threading

def printDigit(digit, char):
    ret = 'print {} {}'.format(digit, char)
    #print('print {}'.format(digit))
    return ret


def gev():
    jobs = [gevent.spawn(printDigit, i, chr(i)) for i in range(97,100)]
    gevent.joinall(jobs)
    print([job.value for job in jobs])                              #通过values获取返回值

if __name__ == '__main__':
    gev()