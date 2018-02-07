#!/usr/bin/python
#coding=utf-8
import os
from multiprocessing import Process, Pipe

def send(pipe):
    pipe.send(['spam'] + [42, 'egg'])
    pipe.close()

def talk(pipe):
    pipe.send(dict(name = 'Bob', spam = 42))
    reply = pipe.recv()
    print('talker got:', reply)

if __name__ == '__main__':
    (con1, con2) = Pipe()
    sender = Process(target = send, name = 'send', args = (con1, ))
    sender.start()
    print("con2 got: %s" % con2.recv())#从send收到消息
    con2.close()

    (parentEnd, childEnd) = Pipe()
    child = Process(target = talk, name = 'talk', args = (childEnd,))
    child.start()
    print('parent got:', parentEnd.recv())
    parentEnd.send({x * 2 for x in 'spam'})
    child.join()
    print('parent exit')