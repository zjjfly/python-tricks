# -*- coding: utf-8 -*-
import common
import math


# Python类中有三种常用的方法：class method，static method，instance method
class MyClass:
    # instance method是最常用的方法，特点是通过对象进行调用，并且第一个参数为当前的对象（调用的时候不用显式传递）
    # 它也可以通过self.__class__来修改类的状态
    def method(self):
        return 'instance method called', self

    # class method的第一个参数是其所属的类型，但只能修改类的状态，不能修改对象的状态
    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    # static method可以接收任意参数，但无法访问类或对象，所以也无法修改它们的状态
    # 它通常用于定义那些和类或对象状态无关的方法，并且把调用方法的主体限定在了当前类和它的对象
    # 它还更容易进行单元测试，因为不需要为其构建类的对象
    @staticmethod
    def staticmethod():
        return 'static method called'


obj = MyClass()
assert 'instance method called', obj == obj.method()
# 也可以显式传递对象
assert 'instance method called', obj == MyClass.method(obj)

assert 'class method called', MyClass == obj.classmethod()
assert 'class method called', MyClass == MyClass.classmethod()

assert 'static method called' == obj.staticmethod()
assert 'static method called' == MyClass.staticmethod()


@common.comparable
class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

    # class method比较适合的场景：定义工厂方法
    @classmethod
    def margherita(cls, radius):
        return cls(radius, ['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls, radius):
        return cls(radius, ['mozzarella', 'tomatoes', 'ham'])


p = Pizza.margherita(4)
assert Pizza(4, ['mozzarella', 'tomatoes']) == p

assert Pizza.circle_area(4) == p.area()
