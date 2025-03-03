# -*- coding: utf-8 -*-
from asserts import assert_throw


# record这种类型的数据结构有固定的字段数量，并且每个字段都有名称，且可能有不同的类型
# 下面是Python中的一些record的实现

# class，但这种方法的缺点是它需要更多的人工才能达到和其他实现一样的效果。
# 如添加新字段到__init__构造器比较烦琐，默认的字符串表示不是很有用，需要自己实现
# 其中的字段是可变的，并且可以随意添加新字段，这一点有时候并不符合需求
# 虽然可以施加更多的访问控制和使用@property产生只读字段，但这也需要写更多的胶水代码
# 而且class往往会有相关的业务逻辑代码，这使得它在技术上不再是一个纯粹的数据类型

class Car:
    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic


# named tuple，这个在之前章节讨论过
# 它和一般的tuple一样是不可变的，其底层是一般的class
# 它占用的内存比一般的class少，和一般的tuple是一致的
# 它还附带一个漂亮的__repr__实现
from collections import namedtuple
from sys import getsizeof

Point = namedtuple('Point', 'x y z')
p1 = Point(1, 2, 3)
p2 = (1, 2, 3)
assert getsizeof(p1) == getsizeof(p2)
# 使用named tuple是相比使用dict更好的存放数据的结构，因为其让代码的可读性和可维护性有很大提高

# types.NamedTuple，它类似namedtuple，但新增了一个可带类型提示的定义语法
# 但类型提示不具强制性，需配合mypy这种类型检查工具方可确保传入的类型和提示的一致
from typing import NamedTuple


class Car2(NamedTuple):
    color: str
    mileage: float
    automatic: bool

# struct.Struct，它可以在Python值和序列化为bytes的C对象之间进行转换
# 例如，可以处理存储在文件中或来自网络的二进制对象
# 它使用一个格式化的类字符串的迷你语言来定义各种C类型的排列，如char,int和long以及它们的unsigned变体
# 这个类型主要用户和C程序之间的数据交换，而不是存放只在Python代码中使用的数据，除了某些对性能有很高有求的程序
# 因为使用这种方式存储原生类型占用的内存较小，但一般这种优化是不必要的
from struct import Struct

MyStruct = Struct('i?f')
data = MyStruct.pack(23, False, 42.0)
assert MyStruct.unpack(data) == (23, False, 42.0)

# types.SimpleNamespace，Python3.3加入，它和dict类似，但提供了对其名称空间的属性访问
# 即可以像访问类字段一样访问其中的key，它也默认包含了一个漂亮的__repr__实现
# 它支持随意地添加，更新和删除字段
from types import SimpleNamespace

car1 = SimpleNamespace(color='red',
                       mileage=3812.4,
                       automatic=True)
print(car1)
car1.mileage = 12
car1.windshield = 'broken'
assert car1.windshield == 'broken'
del car1.automatic
assert_throw(AttributeError, lambda: car1.automatic)
