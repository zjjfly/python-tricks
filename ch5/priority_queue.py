# -*- coding: utf-8 -*-
from bisect import insort

# priority queue，类似queue，但其中的元素有优先级，
# dequeue操作会取出优先级最高或最低的元素，而不是LILO

# list，理论上它也可以作为priority queue
# 但需要每次插入数据都resort整个list，或者使用bisect.insort找到要插入的地方
q = []
insort(q,(2,'code'), key=lambda r: r[0])
insort(q,(1,'eat'), key=lambda r: r[0])
insort(q,(3,'sleep'), key=lambda r: r[0])
while q:
    next_item= q.pop()
    print(next_item)

# heapq，是一个基于list的二叉堆实现，它支持复杂度为O(log n)的插入和获取最小元素
# 它只提供了最小堆的实现，所以需要额外的步骤来保证排序的稳定和作为一个实用的priority queue所需要的其他特性
import heapq
q = []
heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))
while q:
    next_item= heapq.heappop(q)
    print(next_item)

# queue.PriorityQueue，它内部使用了heapq来实现，有相同的时间和空间复杂度
# 它是同步的，可以支持多个生产者和消费者，但这也会导致性能问题，要根据实际场景来评估
# 它是一个基于类的实现，相比于heapq基于函数的实现的使用体验更好
from queue import PriorityQueue
q = PriorityQueue()
q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))
while q:
    next_item= q.get()
    print(next_item)
