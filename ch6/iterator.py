# -*- coding: utf-8 -*-

# Python的for-in语法糖的底层，实际是相关类型实现了__iter__和__next__方法
# 所以任意实现这两个方法的类型，都可以使用for-in语法
# 下面的类Repeater实现了这两个方法，会重复不断的迭代同一个值
class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


repeater = Repeater('Hello')
for r in repeater:
    print(r)
    break

# 可以使用iter和next方法来“模拟”for-in循环
iterator = iter(repeater)
assert next(iterator) == 'Hello'


# iter和next实际调用的就是__iter__和__next__，Python提供这样的内置函数来让代码看起来更加漂亮和易读
# len其实也一样，它实际调用的是__len__方法

# 实际上，__iter__和__next__可以放在一个类中
class Repeater2:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


repeater2 = Repeater2('Hello')
for r in repeater2:
    print(r)
    break


# 怎么实现一个可以停止的iterator？实际上，只要在应该停止的时候抛出StopIteration异常就可以了
class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count == self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value


bp = BoundedRepeater('Hello', 3)
for r in bp:
    print(r)


# Python2和3在iterator上的区别是，Python2中，获取下一个元素的方法叫next，没有前后的双下划线
# 下面是一个兼容2和3的iterator实现
class InfiniteRepeater(object):

    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

    # Python 2 compatibility:
    def next(self):
        return self.__next__()
