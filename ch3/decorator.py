# -*- coding: utf-8 -*-
import functools


# decorator的本质是对callable进行wrap，在其前后加上一些通用的逻辑

# 最简单的decorator
def null_decorator(func):
    print('do nothing')
    return func


def greet():
    """return a friendly greeting."""
    return 'Hello'


decorated_greet = null_decorator(greet)
assert 'Hello' == decorated_greet()


# 可以使用@语法在方法上加上decorator
@null_decorator
def greet2():
    return 'Hello'


assert 'Hello' == greet2()


# 一个把函数输出的字符串改为大写的decorator
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@uppercase
def greet3():
    return 'Hello'


assert 'HELLO' == greet3()


# 不同的decorator可以叠加在一个函数上
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'

    return wrapper


def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'

    return wrapper


@strong
@emphasis
def greet4():
    return 'Hello!'


# 多个decorator的情况下，应用的顺序是自下而上的
assert '<strong><em>Hello!</em></strong>' == greet4()


# 带参数的函数使用decorator
def trace(func):
    # 使用*args捕获position arguments，使用**kwargs捕获keyword arguments
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__qualname__}() ',
              f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__qualname__}() ',
              f''f'returned {original_result!r}')

        return original_result

    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


say('Jane', 'Hello, World')
# TRACE: calling say()  with ('Jane', 'Hello, World'), {}
# TRACE: say()  returned 'Jane: Hello, World'

# 被decorator装饰后的函数无法获取到原来函数的元数据，这会导致debug遇到难题
assert 'wrapper' == say.__name__

assert say.__doc__ is None


# Python内置了一个decorator来解决这个问题，它会复制被装饰的函数的元数据到装饰后的函数
# 实践中，请在每个自定义decorator这使用

def lowercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().lower()

    return wrapper


@lowercase
def greet5():
    """Return a friendly greeting."""
    return 'Hello!'


assert 'greet5' == greet5.__name__
assert 'Return a friendly greeting.' == greet5.__doc__
