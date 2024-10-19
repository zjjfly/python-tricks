# -*- coding: utf-8 -*-

# 随着generator越来越流行， 部分开发者会觉得它还是有点烦琐
# 所以，Python又加入了generator expression来简化它
# 下面是使用它来实现之前的bounded_repeater的例子
iterator = ('Hello' for i in range(3))
for x in iterator:
    print(x)

# 和generator一样，其构造的iterator只能使用一次，重复使用是没有效果的
for x in iterator:
    assert False

# 和list comprehension一样，它也可以在后面加上条件表达式来过滤
even_squares = (x * x for x in range(10) if x % 2 == 0)
for i in even_squares:
    print(i)

# generator expression如果是一个函数的唯一参数，可以去掉外面的括号
assert sum(x * 2 for x in range(10)) == 90

# generator expression可以嵌套，但最好不要超过两层
for i in (x * y for x in range(3)
          for y in range(1,3)):
    print(i)
