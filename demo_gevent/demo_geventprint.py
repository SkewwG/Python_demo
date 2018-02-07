#协程，直接在函数打印内容。函数不return
import gevent

def printDigit(digit):
    print('print {}'.format(digit))

def gev():
    jobs = [gevent.spawn(printDigit,digit) for digit in range(100)]
    gevent.joinall(jobs)

if __name__ == '__main__':
    gev()