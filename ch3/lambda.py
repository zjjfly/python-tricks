# -*- coding: utf-8 -*-

# lambda是Python中定义匿名函数的关键字
add = lambda x, y: x + y
assert 8 == add(5, 3)

# lambda可以直接调用儿不用通过变量
assert (lambda x, y: x + y)(5, 3) == 8

# lambda和函数的另一个区别是它的主体只能是一个表达式，不能有statement，也不能有annotation
# 所以lambda也叫做单表达式函数

# 比较典型的使用场景是作为sorted函数的参数key的值
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
assert [(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')] == sorted(tuples, key=lambda x: x[1])


# lambda也可以作为closure
def make_adder(n):
    return lambda x: x + n


plus_3 = make_adder(3)
assert plus_3(4) == 7

# 尽量少用lambda，除非它确实相比函数更加简洁和易维护
# 如map或filter方法，使用list comprehension或生成器表达式会更好
assert [0, 2, 4, 6, 8, 10, 12, 14] == list(filter(lambda x: x % 2 == 0, range(16)))
# 下面的方式更好
assert [0, 2, 4, 6, 8, 10, 12, 14] == [x for x in range(16) if x % 2 == 0]
