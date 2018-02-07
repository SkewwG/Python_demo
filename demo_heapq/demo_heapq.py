import heapq
import random

# Top-K
mylist = list(random.sample(range(100), 10))
k = 3
largest = heapq.nlargest(k, mylist)
smallest = heapq.nsmallest(k, mylist)
print('original list is', mylist)
print('largest-' + str(k), '  is ', largest)
print('smallest-' + str(k), ' is ', smallest)

# heapify
print('original list is', mylist)
heapq.heapify(mylist)
print('heapify  list is', mylist)

# heappush & heappop
heapq.heappush(mylist, 105)
print('pushed heap is', mylist)
heapq.heappop(mylist)
print('popped heap is', mylist)

# heappushpop & heapreplace
heapq.heappushpop(mylist, 130)  # heappush -> heappop
print('heappushpop', mylist)
heapq.heapreplace(mylist, 2)  # heappop -> heappush
print('heapreplace', mylist)