# -*- coding: utf-8 -*-

# Python会隐式地在函数最后添加一个return None，所以显示用return返回值的函数都返回的是None

# 下面三个函数实际是一样的
def foo1(value):
    if value:
        return value
    else:
        return None


def foo2(value):
    """Bare return statement implies `return None`"""
    if value:
        return value
    else:
        return


def foo3(value):
    """Missing return statement implies `return None`"""
    if value:
        return value

# 对于逻辑上不需要返回值的函数，可以不用显示加上return
# 其他情况下，则要考虑加上或省略return对可读性和可维护性的影响
