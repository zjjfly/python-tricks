# -*- coding: utf-8 -*-
import common
import collections
import typing
import json

tup = ('hello', object(), 42)
assert 42 == tup[2]


def tuple_item_assign():
    tup[2] = 23


# Python的tuple是不可变数据结构，所以对其中的元素重新赋值会报错
common.assert_throw(TypeError, tuple_item_assign)

# 一般的tuple的问题是，只能使用index去访问其中的元素，影响代码的可读性
# 而且，很难保证两个tuple有相同数量的元素并且有相同的值

# 为了解决这些问题，Python2.6的collections模块中加入了named tuple这种数据结构
Car1 = collections.namedtuple('Car', 'color mileage')
# 第一个参数是这个工厂方法用于动态生成的类的名称
# 第二个参数是属性名称列表，如果是字符串则可以用空格或逗号分隔，也可以是字符串的list
Car2 = collections.namedtuple('Car', ['color',
                                      'mileage'])
my_car = Car2('red', 3812.4)
assert 'red' == my_car.color
assert 3812.4 == my_car.mileage


# 3.6之后加入了另外一种定义named tuple的方式：typed named tuple
class Car3(typing.NamedTuple):
    color: str
    mileage: float


my_car = Car3('green', 123.4)
assert 'green' == my_car.color
assert 123.4 == my_car.mileage

# named tuple也可以使用index去访问属性
assert 'green' == my_car[0]
assert 123.4 == my_car[1]

# named tuple也支持tuple unpacking和argument unpacking
color, mileage = my_car
assert 'green' == color
assert 123.4 == mileage


# named tuple也是不可变的，所以无法修改它的属性
def named_tuple_field_assign():
    my_car.color = 'yellow'


common.assert_throw(AttributeError, named_tuple_field_assign)


# 可以把named tuple看成一种定义不可变类型的快捷的方式

# named tuple可以继承，但这种做法比较笨重，不推荐
class MyCarWithMethods(Car1):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'


c = MyCarWithMethods('red', 1234)
assert '#ff0000' == c.hexcolor()

# 最简单的对named tuple继承的做法是使用基tuple的_fields属性
Car4 = collections.namedtuple('Car', 'color mileage')
ElectricCar = collections.namedtuple('ElectricCar', Car4._fields + ('charge',))
print(repr(ElectricCar('red', 1234, 45.0)))
# ElectricCar(color='red', mileage=1234, charge=45.0)

# named tuple自带的一些实用的方法，它们都以下划线开头
# _asdict()可以把tuple的内容转为dictionary
assert {'color': 'green', 'mileage': 123.4} == my_car._asdict()
# 这个方法在把tuple转成JSON的时候很有用，可以避免拼错属性名
assert '{"color": "green", "mileage": 123.4}' == json.dumps(my_car._asdict())

# 还有一个有用的方法是_replace，可以对tuple进行浅拷贝，并在拷贝的时候替换某些属性
some_car = my_car._replace(color='blue')
assert 'blue' == some_car.color
assert 123.4 == some_car.mileage

# 最后一个方法是_make，可以使用一个序列来构造一个named tuple实例
assert Car1('red', 999) == Car1._make(['red', 999])

# 有些时候，使用named tuple来代替dictionary可以让你的代码更清晰和更易于维护
