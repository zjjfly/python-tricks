# -*- coding: utf-8 -*-

# Python中没有switch case语法，但我们可以使用dict和函数可以作为值这一特性来模拟
# 下面是原始的代码，使用if-else语法
def handle_a():
    return 'a'


def handle_b():
    return 'b'


def handle_default():
    return 'xyz'


cond = 'cond_b'
if cond == 'cond_a':
    handle_a()
elif cond == 'cond_b':
    handle_b()
else:
    handle_default()


def myfunc(a, b):
    return a + b


func_dict = {
    'cond_a': handle_a,
    'cond_b': handle_b,
}
f = func_dict.get(cond, handle_default)
assert 'b' == f()


# 下面是一个更复杂和实际的例子：
def dispatch_dict(operator, x, y):
    return {
        'add': operator,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()
assert dispatch_dict('mul', 2, 8) == 16
assert dispatch_dict('unknown', 2, 8) is None
