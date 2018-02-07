import heapq

l = [0, 19, 28, 61, 34, 57, 42, 95, 70, 51]
def heapsort(l):
    h = []
    for i in l:
        heapq.heappush(h,i)                         #heapq.heappush往h里添加i
    return h
h = heapsort(l)
print(h)


heapq.heapify(l)
print('l 的类型 : {}  {}'.format(type(l),l))        #堆的类型也是列表，heapq.heapify将列表转换为堆

print('nlargest :',heapq.nlargest(3,h))             #heapq.nlargest取最大的几个数
print('nsmallest :',heapq.nsmallest(3,h))           #heapq.nsmallest取最小的几个数

heapq.heappushpop(h,22)                             #heapq.heappushpop      heappush -> heappop
print('heappushpop : ',h)

heapq.heapreplace(h,1)                              #heapq.heapreplace      heappop -> heappush
print('heapreplace : ',h)

for i in range(len(h)):
    print(h[i],end=',')                             #h[i].堆也可以通过下标查看
print()

#利用heappop进行排序
l1 = []
for i in range(len(h)):
    l1.append(heapq.heappop(h))                     #heapq.heappop从h里弹出最小值
print(l1)


