#实现优先级队列

import heapq

class PriorityQueue():
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        # -priority是为了优先级能够从高到低的顺序排列
        # self._index这个额外的索引值，是为了避免当优先级一样时程序报错。此时会以插入顺序而弹出
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item():
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)       # 为了打印的内容是字符串，而不是类型。否则传到队列里是类型值

q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)
print(q._queue)
print(q.pop())
print(q._queue)
print(q.pop())
print(q._queue)
print(q.pop())
print(q._queue)
print(q.pop())
print(q._queue)