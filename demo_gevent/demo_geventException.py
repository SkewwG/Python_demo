#协程状态和异常
#设计属性：started,ready(),value,successful(),exception
import gevent

def success():
    print('You success!')

def fail():
    raise Exception('You failed!')

winner = gevent.spawn(success)
loser = gevent.spawn(fail)

print('winner协程状态是否开启 ：',winner.started)
print('loser协程状态是否开启 ：',loser.started)

try:
    gevent.joinall([winner,loser])
except Exception as e:
    print('This will never be reached')

print('winner协程状态是否关闭 ：',winner.ready())
print('loser协程状态是否关闭 ：',loser.ready())

print('winner协程return返回值 ：',winner.value)
print('loser协程return返回值 ：',loser.value)

print('winner协程成功运行且没有异常 ：',winner.successful())
print('loser协程成功运行且没有异常 ：',loser.successful())

#协程运行过程中发生的异常是不会被抛出到协程外的，因此需要用协程对象的”exception”属性来获取协程中的异常
print('loser协程抛出异常 ：',loser.exception)