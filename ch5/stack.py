# -*- coding: utf-8 -*-
from common import assert_throw

# stack是一个先进后出的数据结构，主要支持两个操作：push和pop，并且它们的复杂度都是O(1)
# Python中有多个stack的实现，下面逐一介绍：

# list，它有pop方法，并且它的append方法相等于push
# 由于其底层存储是一个动态数组，会动态改变大小，所以其性能并不能稳定
# 栈顶对应list的最后的一个元素，这样的性能比把首个元素作为栈顶在性能上好很多
# 它的优点是提供了O(1)的随机元素访问
s = []
s.append('eat')
s.append('sleep')
s.append('code')
assert s.pop() == 'code'
assert s.pop() == 'sleep'
assert s.pop() == 'eat'
assert_throw(IndexError, lambda : s.pop())

# collection.deque，它是一个双端队列，并且两端都支持O(1)复杂度的添加和删除元素
# 所以它既可以作为stack也可以作为queue，它的缺点随机元素访问的复杂度是O(n)
from collections import deque
s = deque()
s.append('eat')
s.append('sleep')
s.append('code')
print(s)
assert s.pop() == 'code'
assert s.pop() == 'sleep'
assert s.pop() == 'eat'
assert_throw(IndexError, lambda : s.pop())

# queue.LifoQueue，它支持多个并发的生产者/消费者，queue这个包中的其他类也支持多生产者/消费者
# 它内部使用的锁来控制并发，所以性能方面不算高，如不存在并发不要用它
from queue import LifoQueue
s = LifoQueue()
s.put('eat')
s.put('sleep')
s.put('code')
print(s)
assert s.get() == 'code'
assert s.get() == 'sleep'
assert s.get() == 'eat'

