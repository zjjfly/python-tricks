# -*- coding: utf-8 -*-

# Python中的==相当于Java的equals，is相当于Java的==
a = [1, 2, 3]
b = a

assert a == b

assert a is b

# 使用list函数拷贝a，产生的是一个新的对象
c = list(a)

assert a == c

assert a is not c
