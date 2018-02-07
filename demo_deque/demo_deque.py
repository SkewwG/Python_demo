#双向队列
from collections import deque

print(dir(deque))

d = deque()
d.append([1,1,1,1])                                         #append与extend的区别
d.extend([2,2,2,2,2,2,3,4])

print('[1]append : {}'.format(d))

d.appendleft(5)
print('[2]appendleft : {}'.format(d))

d.extendleft([5,6,7,8])                                     #extendleft(从队列左边扩展一个列表的元素)
print('[3]extendleft : {}'.format(d))

count_d = d.count(2)                                        #返回指定元素出现的次数
print('[4]count : {}'.format(count_d))

pop_d = d.pop()                                             #pop（获取最右边一个元素，并在队列中删除）
print('[5]pop : {}'.format(pop_d))

popleft_d = d.popleft()                                     #popleft（获取最左边一个元素，并在队列中删除）
print('[6]popleft : {}'.format(popleft_d))

d.remove(2)                                                 #remove（删除指定元素）
print('[7]remove : {}'.format(d))

d.reverse()                                                 #reverse（队列反转）
print('[8]reverse : {}'.format(d))

d.rotate(3)                                                 #rotate（把右边元素放到左边）
print('[9]rotate : {}'.format(d))

d.clear()
print('[10]clear : {}'.format(d))