# -*- coding: utf-8 -*-
from contextlib import contextmanager
import time

with open('hello1.txt', 'w') as f:
    f.write('Hello,World!')


# 让自定义的类支持with语法
class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with ManagedFile('hello2.txt') as f:
    f.write('Hello,World!\n')
    f.write('Bye!')


# 让自定义的方法支持with语法
@contextmanager
def managed_file(name):
    try:
        file = open(name, 'w')
        yield file
    finally:
        file.close()


with managed_file('hello3.txt') as f:
    f.write('Hello,World!\n')
    f.write('bye now')


# 利用context manager写出更漂亮的代码
class Indent:
    def __init__(self):
        self.indentSize = 0
        self.entered = False
        return

    def __enter__(self):
        if self.entered:
            self.indentSize += 1
        self.entered = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.indentSize:
            self.indentSize -= 1

    def print(self, s):
        indent_str = '\t' * self.indentSize
        print(indent_str + s)


with Indent() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello')
        with indent:
            indent.print('bonjour')
    indent.print('hey')


# exercise
class MeasureExecutionTime:
    def __init__(self):
        self.start_time = 0
        return

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        execution_time = end_time - self.start_time
        print("execution time:%s" % execution_time)


with MeasureExecutionTime():
    sum = 0
    for i in range(100000):
        sum += i
    print(sum)


@contextmanager
def measure_execution_time():
    try:
        start_time = time.time()
        yield 1
    finally:
        end_time = time.time()
        execution_time = end_time - start_time
        print("execution time:%s" % execution_time)


with measure_execution_time():
    sum = 0
    for i in range(100000):
        sum += i
    print(sum)
