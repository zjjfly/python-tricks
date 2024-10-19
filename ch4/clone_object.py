# -*- coding: utf-8 -*-
import copy
import common

# 可以使用工厂方法对Python的可变集合进行浅拷贝
original_list = [1, 2, 3]
new_list = list(original_list)
assert original_list == new_list

original_set = {1, 2, 3}
new_set = set(original_set)
assert original_set == new_set

original_dict = {'a': 1, 'b': 2}
new_dict = dict(original_dict)
assert original_dict == new_dict

# 浅拷贝的问题是，如果改变了原对象的某个子对象，拷贝对象的子对象也会一起跟着修改，因为实际上它们指向的是相同的内存地址
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)
assert xs == ys

xs.append(['new sublist'])
assert xs != ys

xs[1][0] = 'x'
assert xs[1] == ys[1]

# 深度拷贝可以使用copy这个包里的deepcopy函数实现
zs = copy.deepcopy(xs)
assert zs == xs

xs[1][0] = 'X'
assert xs[1] != zs[1]


# 拷贝自定义类的对象

@common.comparable
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'


# 如果类的属性都是primitive type，使用浅拷贝或深拷贝是没有区别的
a = Point(1, 2)
b = copy.copy(a)
assert a == b


@common.comparable
class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, '
                f'{self.bottomright!r})')


# 对于属性的类型有非primitive type的，或是非primitive type的集合的，需要使用深拷贝
rect = Rectangle(Point(0, 1), Point(5, 6))
drect = copy.deepcopy(rect)
drect.topleft.x = 222
assert rect.topleft != drect.topleft
