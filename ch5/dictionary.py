# -*- coding: utf-8 -*-
from logging import fatal

from asserts import assert_throw

# Python中Map的实现是dict这个类，是Python的核心的数据结构之一
# 所以Python提供了一些相关的语法糖
# 如便利的字面量语法：
phonebook = {
    'bob': 7387,
    'alice': 3719,
    'jack': 7052,
}

assert phonebook['alice'] == 3719

squares = {x: x * x for x in range(6)}
assert squares == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# dict对key值的类型是有限制的，它必须是hashable的
# hashable的定义是：这个对象有一个在其生命周期中不会改变的hash值(__hash__方法)，
# 它可以和其他对象进行比较(__eq__方法)，且相等的两个对象的hash值必然相等
# 不可变类型如字符串和数字是hashable的，tuple也可以作为dict的key，只要其中的元素都是hashable的

# dict是经过高度优化的，并作为Python语言很多部分的底层，如类的属性和栈帧的变量都是放在一个dict中。
# 它基于一个经过充分测试和微调的hash table实现，提供了我们想要的性能：一般情况下O(1)复杂度的查询，插入，更新和删除操作
# 很少需要使用除了它之外的其他Map实现，但确实有一些第三方的实现，如基于skip list或B-Tree的实现

# 除了普通的dict类，Python中还有一些有专门作用的Map，这些Map都是基于dict类型，但在其之上添加了一些便利的特性

# collections.OrderDict，类似Java中的LinkedHashMap，可以保持键值对的存入顺序
# 虽然在CPython3.6的时候dict已经可以做到这一点，但这个特性并不在Python规范中，所以可能其他Python实现的dict并没有此特性
# 如果保持键值对的存入顺序这一点很重要，最好还是使用这个类
from collections import OrderedDict

d = OrderedDict(one=1, two=2, three=3)
print(d.keys())

# collections.defaultdict，这个类的构造器可以传入一个callable来设置当key找不到时的默认返回
# 这相比于使用get方法或捕获KeyError更加简单
from collections import defaultdict

dd = defaultdict(list)
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')
assert dd['dogs'] == ['Rufus', 'Kathrin', 'Mr Sniffles']

# collections.ChainMap，它可以实现像查询单个dict一样查询多个dict
# 但对于插入，更新和删除操作，只会对第一个dict起作用
from collections import ChainMap

dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = ChainMap(dict1, dict2)

assert chain['one'] == 1
assert chain['three'] == 3
assert_throw(KeyError, lambda: chain['missing'])

# types.MappingProxyType，它可以包装一个dict，把它变成一个只读的dict
from types import MappingProxyType

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)
assert read_only['one'] == 1
try:
    read_only['one']= 23
    assert False
except TypeError as e:
    print(e)
# 对原dict的修改会反映到MappingProxyType中
writable['one']= 42
assert read_only['one'] == 42
