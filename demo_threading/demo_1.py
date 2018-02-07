#-*- coding:utf-8 -*-
import socket
import threading

def portScan():
    tgtHost = '10.228.0.30'
    tgtPort = 445
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((tgtHost,tgtPort))
        print('[+] {0} {1} open'.format(tgtHost,tgtPort))
    except Exception as e:
        print('[-] {0} {1} closed : {2}'.format(tgtHost,tgtPort,e))

if __name__ == '__main__':
    portScan()