# -*- coding: utf-8 -*-

# dict没有固有的顺序，无法保证遍历按照某种顺序返回元素
# 但往往很多时候按照某种顺序便利dict是很有用的，这种情况可以考虑对dict的items方法返回的tuple列表进行排序
xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
sorted_items = sorted(xs.items())
assert sorted_items == [('a', 4), ('b', 3), ('c', 2), ('d', 1)]

# sorted是按照词典顺序进行排序的，对于tuple是首先对tuple的第一个元素排序，如果一样就用第二个元素排序......
# 如果想要对排序行为进行定制，可以传入一个key函数，即一个返回用于排序的值的函数
# 下面的代码就是按照dict的value排序的例子：
sorted_items = sorted(xs.items(), key=lambda x: x[1])
assert sorted_items == [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# key函数在Python标准库中很普遍，但不限于排序，可以把它看成是一个把传入的值根据某些规则转成另一个值的函数
# 在operator这个module中有很多现成的key函数，下面使用其中的itemgetter来实现和刚刚一样的功能
import operator

sorted_items = sorted(xs.items(), key=operator.itemgetter(1))
assert sorted_items == [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# 使用operator中的函数在某些情况会让你的意图更加清晰，而使用lambda表达式更加易读和简洁，实践中更加推荐后者
# 使用lamda表达式的另一个好处是对排序可以有更加精细的控制，比如按照dict的value的绝对值排序
xs = {'a': 4, 'c': 2, 'b': -3, 'd': -1}
sorted_items = sorted(xs.items(), key=lambda x: abs(x[1]))
assert sorted_items == [('d', -1), ('c', 2), ('b', -3), ('a', 4)]

# sorted函数的可以传入第三个参数来控制正序还是倒序
sorted_items = sorted(xs.items(), key=lambda x: abs(x[1]), reverse=True)
assert sorted_items == [('a', 4), ('b', -3), ('c', 2), ('d', -1)]
