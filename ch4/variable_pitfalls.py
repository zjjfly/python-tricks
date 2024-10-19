# -*- coding: utf-8 -*-
import common


# Python的variable分为class variable和instance variable
# 可以和Java的静态成员变量和一般成员变量

class Dog:
    num_legs = 4  # <- Class variable

    def __init__(self, name):
        self.name = name  # <- Instance variable


jack = Dog('Jack')
jill = Dog('Jill')
assert ('Jack', 'Jill') == (jack.name, jill.name)
assert jack.num_legs == jill.num_legs == 4
# 无法通过类获取instance variable
common.assert_throw(AttributeError, lambda: Dog.name)

# 但可以通过为对象添加和class variable同名的instance variable来shadow它
# 这也算是Python的OOP的一个缺陷
jack.num_legs = 6
assert jack.num_legs == 6
assert jill.num_legs == 4


# class variable的用法
class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1

    # 下面的这种实现就是错误的，因为self.num_instances是instance variable
    # def __init__(self):
    #     self.num_instances += 1


assert 0 == CountedObject.num_instances
assert 1 == CountedObject().num_instances
assert 2 == CountedObject().num_instances
