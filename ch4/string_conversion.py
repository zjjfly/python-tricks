# -*- coding: utf-8 -*-
import datetime


class Car1:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


my_car = Car1('red', 37281)

# 打印自定义类的对象，默认的实现的可读性比较差，和Java类似
print(my_car)


# <__main__.Car object at 0x102aa8eb0>

# Python有一个内置的方法__str__，类似Java的toString，会在程序视图对象转成字符串的调用


class Car2:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'a {self.color} car'


my_car = Car2('red', 37281)
print(my_car)
# a red car
assert 'a red car' == str(my_car)
assert 'a red car' == '{}'.format(my_car)


# 还有一个内置函数__repr__，类似__str__
class Car3:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return '__str__ for Car'

    def __repr__(self) -> str:
        return '__repr__ for Car'


my_car = Car3('red', 37281)

# 什么时候调用__repr__?
# 首先是在Python解释器对某个对象进行inspect的时候
# my_car
# 还有是在打印list或dict的时候
cars = [Car3('red', 1), Car3('green', 2)]
print(cars)
# [__repr__ for Car, __repr__ for Car]
# 即使调用str也是同样的结果
assert '[__repr__ for Car, __repr__ for Car]' == str(cars)
# 所以最好的方式是显式地使用str或repr函数来明确要使用的实现
assert '__str__ for Car' == str(my_car)
assert '__repr__ for Car' == repr(my_car)

# __repr__和__str__的区别是，它主要是为了帮助开发人员debug
# 可以通过Python标准库中对其的使用来说明这一点
today = datetime.date.today()
# assert '2023-06-05' == str(today)
assert f'datetime.date({today.year}, {today.month}, {today.day})' == repr(today)


# 当__str__没有实现的时候，Python解释器会调用__repr__，所以推荐为每个自定义的类实现__repr__
class Car4:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # 一个比较通用的实现
    def __repr__(self):
        args = []
        for (k, v) in self.__dict__.items():
            args.append(f'{k}={v!r}')
        s = ','.join(args)
        # !r在formatted string literal中的作用是使用对象的__repr__方法来表示对象
        return f'{self.__class__.__name__}({s})'


assert "Car4(color='red',mileage=1)" == str(Car4('red', 1))
