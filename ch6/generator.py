# -*- coding: utf-8 -*-
from typing import Generator


# 相比于使用class实现iterator，Python还提供了一种更加简洁的方式：generator
# 下面是使用generator来实现的一个无限重复的迭代器
def repeater(value):
    while True:
        yield value


for x in repeater('Hi'):
    print(x)
    break

# 看上去generator就是一个简单的函数，实际它返回的是一个Generator对象，它是一个Iterator的抽象模板
assert isinstance(repeater('Hey'), Generator)

# 函数体的代码只有在调用generator的__next__方法的时候才调用
generator_obj = repeater('Hey')
assert next(generator_obj) == 'Hey'

# yield关键字看着像把函数的执行暂停，在之后的某个时间点继续执行
# 其实这个想法和实际发生的很接近，yield和return都会把控制权交还给调用者，但和return不同的是，yield是暂时的
# yield会把本地状态存储起来，一边之后继续执行，这样使得generator能够和iterator协议兼容，也因此可以把generator看出实现iterator的语法糖
iterator = repeater('Hi')
assert 'Hi' == next(iterator)
assert 'Hi' == next(iterator)
assert 'Hi' == next(iterator)


# 如何停止generator？只要不通过yield从函数中返回就可以了
def repeat_three_times(value):
    yield value
    yield value
    yield value


for x in repeat_three_times('Hey there'):
    print(x)

# 下面使用generator来实现BoundedRepeater
def bounded_repeater(value,max_repeats):
    for _ in range(max_repeats):
        yield value

for x in bounded_repeater('Hi', 4):
    print(x)

# generator在内存角度上来说是高效的，因为它只有当实际调用next的时候才会执行方法体来计算要返回的值
