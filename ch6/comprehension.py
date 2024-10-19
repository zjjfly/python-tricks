# -*- coding: utf-8 -*-

# list comprehension，其实是一种更紧凑和简洁的循环语法
squares = [x * x for x in range(10)]
assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 它等价于下面的代码
squares = []
for i in range(10):
    squares.append(i * i)

# list comprehension中可以带条件表达式，从而过滤掉源数据结构中的部分元素
even_squares = [x * x for x in range(10) if x % 2 == 0]
assert even_squares == [0, 4, 16, 36, 64]

# set和dictionary也是支持comprehension的
s = {x * x for x in range(-9, 10)}
print(s)
m = {x: x * x for x in range(5)}
print(m)

# 但要注意，不要写太复杂的comprehension，不然有损代码的可读性
