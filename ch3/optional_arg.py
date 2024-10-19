# -*- coding: utf-8 -*-
import functools


# *args和**kwargs都是用于声明函数的可选参数
# 前者是positional argument，后者是keyword argument
def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


# 在函数中，args是一个tuple，kwargs是一个dict
# 如果没有传入任何可选参数，那么args和kwargs都为空


foo('hello')
# hello
foo('hello', 1, 2, 3)
# hello
# (1, 2, 3)
foo('hello', 1, 2, 3, key1='value', key2=999)


# hello
# (1, 2, 3)
# {'key1': 'value', 'key2': 999}

# args和kwargs只是惯用的变量名，不是必要的

# 可以对args和kwargs进行unpack，传给另一个接收可选参数的函数
def foo2(x, *args, **kwargs):
    kwargs['name'] = 'Alice'
    new_args = args + ('extra',)
    foo(x, *new_args, **kwargs)


foo2('hello')


# hello
# ('extra',)
# {'name': 'Alice'}

# 这一点在子类继承和wrapper函数里很有用
# 下面是继承的例子：
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'


# AlwaysBlueCar的构造函数可以传入任意参数，并把它们传递给父类的构造器
# 这样就可以避免在父类构造器的签名修改之后的兼容问题
# 但这种方式的问题是，子类构造器的签名会让人不知道要传入什么参数
# 所以，它一般不用于我们自己的类之间的继承的时候，而是用于对外部的类进行修改或重载它的某些行为的时候

# 下面是wrapper函数的例子
def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)

    return decorated_function


@trace
def greet(greeting, name):
    return '{}, {}!'.format(greeting, name)


greet('Hello', 'Bob')
# <function greet at 0x100571240> ('Hello', 'Bob') {}
# Hello, Bob!
