# -*- coding: utf-8 -*-

# iterator对象之间是可以串联起来的，这样就可以构建一个处理数据的pipeline
def integers():
    for i in range(1, 9):
        yield i


chain = integers()
assert list(chain) == [1, 2, 3, 4, 5, 6, 7, 8]


# 可以把iterator看成是一个数据的stream，一个stream可以作为另一个stream的输入
def squared(seq):
    for i in seq:
        yield i * i


chain = squared(integers())
assert list(chain) == [1, 4, 9, 16, 25, 36, 49, 64]


def negated(seq):
    for i in seq:
        yield -i


chain = negated(squared(integers()))
assert list(chain) == [-1, -4, -9, -16, -25, -36, -49, -64]

# 这种方法的好处是：输入的元素是一个一个地经过pipeline然后输出的，在不同步骤之间没有缓冲
# 要继续扩展pipeline的处理流程也很容易，修改其中某个步骤也是，因为每一步都是一个单独的generator函数

# 还可以直接是用generator expression来简化代码
integers = range(8)
squared = (i * i for i in integers)
negated = (-i for i in squared)
assert list(negated) == [0, -1, -4, -9, -16, -25, -36, -49]

# 使用generator expression不好的地方是，无法像generation函数那样使用参数来配置generator，而且无法在重复使用
