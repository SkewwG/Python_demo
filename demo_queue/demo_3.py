#-*- coding: utf-8 -*-
import threading
import time

# 建立不同线程的任务，事件的is_set()方法判断当前事件标志
# 如果事件标志为False，执行wait()才会阻塞
# 如果事件标志为Ture，则不会阻塞
# event.set()方法可以将事件标志设置为Ture
# event.clear()方法可以将事件标志设置为False
def man(event):
    if not event.is_set() :
        print("Hello Lancy, nice to meet you.")
        event.wait()
        print("How about to watch a movie together?")
    else:
        event.clear()

def woman(event):
    if not event.is_set() :
        print("Hello Mike, today is a nice day!")
        event.wait()
        print("Let's go!")
    else:
        event.clear()

# 建立各种事件
man_talk_event = threading.Event()
woman_talk_event = threading.Event()

# 创建线程,不同线程对应不同事件
# 如果在start()之前设置t1.setDaemon(True)则不阻塞主线程，后台运行
t1 = threading.Thread(target=man, args=(man_talk_event,), name='man')
t2 = threading.Thread(target=woman, args=(woman_talk_event,), name='woman')
# t1.setDaemon(True)
# t2.setDaemon(True)

# 启动线程，线程会阻塞在event.wait()那里，直到对应事件调用event.set()
t1.start()
time.sleep(1)
t2.start()
time.sleep(1)

# 对应事件的set()方法将事件标志设置为True，则不阻塞线程
# clear()将事件的标志设为False
# 让man继续线程，并最后结束man线程
man_talk_event.set()
time.sleep(1)
man_talk_event.clear()

# 让woman继续线程，并最后结束woman线程
woman_talk_event.set()
time.sleep(1)
woman_talk_event.clear()