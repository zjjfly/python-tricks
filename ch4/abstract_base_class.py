# -*- coding: utf-8 -*-
import asserts
import abc


# abstract base class可以保证派生类实现特定的方法

# 自己实现一个abc
class Base:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()


# 具体实现类,故意没有实现bar方法
class Concrete(Base):
    def foo(self):
        return 'foo() called'


b = Base()
common.assert_throw(NotImplementedError, lambda: b.foo())
c = Concrete()
assert 'foo() called' == c.foo()
common.assert_throw(NotImplementedError, lambda: c.bar())


# 这种实现有两个问题：1.可以初始化基类，2.无法保证派生类实现了所有需要实现的方法
# 所以需要使用Python内置的abc模块
class Base2(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def foo(self):
        pass

    @abc.abstractmethod
    def bar(self):
        pass


# 具体实现类,故意没有实现bar方法
class Concrete2(Base2):
    def foo(self):
        pass


assert issubclass(Concrete2, Base2)
# 初始化派生类的时候，如果它没实现基类的抽象方法，则会报错
common.assert_throw(TypeError, lambda: Concrete2())
