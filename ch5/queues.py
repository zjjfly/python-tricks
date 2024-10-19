# -*- coding: utf-8 -*-
# queue，先进先出的数据结构，支持的操作是enqueue和dequeue
# 它一般不支持随机访问其中的元素

# list，它也可以作为queue使用，但性能非常差
# 因为queue的特性决定了必须要对list的头部插入或删除元素，这个操作的性能并不好
# 除非确定其中的元素会比较少，否则不推荐使用
q = []
q.append('eat')
q.append('sleep')
q.append('code')
assert q.pop(0) == 'eat'

# collections.deque，在stack的时候已经介绍过，是你使用queue的时候的首选
from collections import deque

q = deque()
q.append('eat')
q.append('sleep')
q.append('code')
assert q.popleft() == 'eat'
assert q.popleft() == 'sleep'
assert q.popleft() == 'code'

# queue.Queue，是之前提到的LifoQueue的父类，它支持异步的插入和取出
import queue

q = queue.Queue()
q.put('eat')
q.put('sleep')
q.put('code')
assert q.get() == 'eat'
assert q.get() == 'sleep'
assert q.get() == 'code'

# multiprocessing.Queue，这个是一个shared job queue,可以被多个worker并发地处理
# 基于进程的并行处理在CPython中比较流行，因为GIL阻止了在单个解释器进程中的一些形式的并行处理
# 所以这个queue在多个进程之间共享数据，把工作分派到不同的进程中来绕过GIL的限制
import multiprocessing
q = multiprocessing.Queue()
q.put('eat')
q.put('sleep')
q.put('code')
assert q.get() == 'eat'
assert q.get() == 'sleep'
assert q.get() == 'code'
