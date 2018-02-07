import heapq
def heapsort(iterable):
    h = []
    for i in iterable:
        heapq.heappush(h, i)
    return [heapq.heappop(h) for i in range(len(h))]

# method 1: sort to list
s = [3, 5, 1, 2, 4, 6, 0, 1]
print(heapsort(s))
'''
[0, 1, 1, 2, 3, 4, 5, 6]
'''

# method 2: use key to find price_min
portfolio = [{'name': 'IBM', 'shares': 100, 'price': 91.1},
             {'name': 'AAPL', 'shares': 50, 'price': 543.22},
             {'name': 'FB', 'shares': 200, 'price': 21.09},
             {'name': 'HPQ', 'shares': 35, 'price': 31.75},
             {'name': 'YHOO', 'shares': 45, 'price': 16.35},
             {'name': 'ACME', 'shares': 75, 'price': 115.65}]
cheap = heapq.nsmallest(1, portfolio, key=lambda s:s['price'])
print(cheap)
'''
[{'name': 'YHOO', 'shares': 45, 'price': 16.35}]
'''

# method 3: use while to push min element
def heapilize_list(x):
    n = len(x)
    # 获取存在子节点的节点 index 列表，并对每个节点单元进行最小堆处理
    for i in reversed(range(n // 2)):
        raiseup_node(x, i)

def put_down_node(heap, startpos, pos):
    current_item = heap[pos]
    # 判断单元中最小子节点与父节点的大小
    while pos > startpos:
        parent_pos = (pos - 1) >> 1
        parent_item = heap[parent_pos]
        if current_item < parent_item:
            heap[pos] = parent_item
            pos = parent_pos
            continue
        break
    heap[pos] = current_item

def raiseup_node(heap, pos):
    heap_len = len(heap)
    start_pos = pos
    current_item = heap[pos]
    left_child_pos = pos * 2 + 1
    while left_child_pos < heap_len:
        right_child_pos = left_child_pos + 1
        # 将这个单元中的最小子节点元素与父节点元素进行位置调换
        if right_child_pos < heap_len and not heap[left_child_pos] < heap[right_child_pos]:
            left_child_pos = right_child_pos
        heap[pos] = heap[left_child_pos]
        pos = left_child_pos
        left_child_pos = pos * 2 + 1
    heap[pos] = current_item
    put_down_node(heap, start_pos, pos)

p = [4, 6, 2, 10, 1]
heapilize_list(p)
print(p)
'''
[1, 4, 2, 10, 6]
'''