# -*- coding: utf-8 -*-
# 函数在Python是一等公民
import asserts


def yell(text):
    return f'{text.upper()}!'


# 函数在Python中是对象

# 函数可以赋值,本质上只是新增了一个别名,底层的函数对象不变.
bark = yell
assert bark('woof') == 'WOOF!'

# 函数和名字是独立的，所以即使删除了yell，还是可以使用bark访问
del yell
common.assert_throw(NameError, lambda: yell('hello!'))
assert bark('hey') == 'HEY!'

# 函数产生的时候有一个内部的标识符
assert bark.__name__ == 'yell'
# 3.3之后通过__qualname__访问,以和类名做区别(__name__一般访问的是类名)
assert bark.__qualname__ == 'yell'

# 函数可以在数据结构中存储
funcs = [bark, str.lower, str.capitalize]
assert funcs[0]('heyho') == 'HEYHO!'


# 函数可以作为参数传入别的函数
def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)


greet(bark)


def whisper(text):
    return text.lower() + '...'


greet(whisper)

# 接受函数作为参数的函数也叫做高阶函数
# python内置的map函数就是一个例子
assert list(map(bark, ['hello', 'hey', 'hi'])) == ['HELLO!', 'HEY!', 'HI!']


# 函数是可以嵌套的，被称为嵌套函数或内部函数
def speak(text):
    def shout(t):
        return t.lower()

    return shout(text)


assert speak('Hello, World') == 'hello, world'

# 内部函数是无法在外部访问的
common.assert_throw(NameError, lambda: shout())


# 函数是可以作为返回值的，所以如果想要访问内部函数，可以通过把它作为返回值实现
def get_speak_func(volume):
    def _whisper(text):
        return text.lower() + '...'

    def _yell(text):
        return text.upper() + '!'

    if volume > 0.5:
        return _yell
    else:
        return _whisper


speak_func = get_speak_func(0.7)
assert speak_func('Hello') == 'HELLO!'


# 函数可以捕获它所在上下文中的local stat，也就是闭包(closure)
def make_adder(n):
    def add(x):
        return x + n

    return add


plus_3 = make_adder(3)
plus_5 = make_adder(5)
assert 7 == plus_3(4)
assert 9 == plus_5(4)


# 实现了__call__方法的对象都是callable，可以作为函数
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


plus_3 = Adder(3)
assert 7 == plus_3(4)

# 可以使用callable这个内置函数判断对象是否是callable
assert callable(plus_3)
assert callable(bark)
assert not callable(1)
