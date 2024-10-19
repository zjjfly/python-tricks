# -*- coding: utf-8 -*-
from ch2.my_module import *
import common


# 单下划线开头，一般是意味着该变量或方法只在类的内部使用
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23


test = Test()
assert 11 == test.foo
assert 23 == test._bar

assert 23 == external_func()

# 如果不使用wildcard import,而是用import ch2.my_module导入模块，那么_internal_func是可以导入的
common.assert_throw(NameError, lambda: _internal_func())


# 单下划线结尾，一般是为了避免命名和python关键字的冲突
def make_object(name, class_):
    pass


# 双下划线开头，会让解释器对该变量或方法的名字进行重写来防止子类中的成员会和它产生命名冲突，类似Clojure的Macro中的"#"后缀
# 这种做法叫作name mangling
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23


t = Test()
print(f"dir(t):{dir(t)}")


class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'


t2 = ExtendedTest()
assert 'overridden' == t2.foo
assert 'overridden' == t2._bar
# 下面的代码会报错:AttributeError: 'ExtendedTest' object has no attribute '__baz'，因为被重写后的名称是_Test__baz
common.assert_throw(AttributeError, lambda: t2.__baz)
print(f"dir(t2):{dir(t2)}")
assert 23 == t2._Test__baz
assert 'overridden' == t2._ExtendedTest__baz


# 这种重写在内的内部是对开发人员透明的
class ManglingTest:
    def __init__(self) -> None:
        self.__mangled = 'hello'

    def get_mangled(self):
        return self.__mangled


mt = ManglingTest()
assert 'hello' == mt.get_mangled()


# 方法也同样

class MangledMethod:
    def __method(self):
        return 42

    def call_it(self):
        return self.__method()


mm = MangledMethod()
assert 42 == mm.call_it()

common.assert_throw(AttributeError, lambda: mm.__method())
# AttributeError: 'MangledMethod' object has no attribute '__method'

_MangledGlobal__mangled = 11


class MangledGlobal:
    def test(self):
        return __mangled


# 如果在类的内部找不到变量，会在全局查找（以重写后的名称），所以下面的断言是成立的
assert 11 == MangledGlobal().test()


# 双下滑线开头和结尾，表示是python保留的一些特殊用途的变量或函数，典型的如__init__和__call__
# 一般避免使用这种类型的命名方式
class PrefixPostfixTest:
    def __init__(self) -> None:
        self.__bam__ = 42


assert 42 == PrefixPostfixTest().__bam__

# 单下划线，表示是一个无关紧要的变量，类似Go或Scala的用法
for _ in range(3):
    print('Hello,World')

car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car
assert 'red' == color
assert 3812.4 == mileage
