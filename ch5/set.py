# -*- coding: utf-8 -*-
from common import assert_throw

# set，和dict一样有字面量语法
vowels = {'a', 'e', 'i', 'o', 'u'}
# 它还有comprehensions语法
squares = {x * x for x in range(10)}
# 空set需要调用set的构造器，因为空的{}产生的是一个空的dict
emtpy = set()
# 下面是标准库中的set的几种实现

# set，这是默认的set实现，它底层是使用的dict，所以在性能方面和它一致
# 任意hashable的值都可放入set，但其本身不是hashable的，因为它在初始化之后还可以加入新元素
# 判断某个元素是否在set中
assert 'e' in vowels
letters = set('alice')
assert letters.intersection(vowels) == {'a', 'e', 'i'}

vowels.add('x')
assert len(vowels) == 6

# frozenset，它是set的不可变版本，且是hashable的，所以可以作为dict的key
vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
assert_throw(AttributeError, lambda: vowels.add('x'))

# collections.Counter，它是multiset的一种实现
# multiset的特点是元素在其中可以重复出现
from collections import Counter

inventory = Counter()
loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
assert inventory.get('bread') == 3
more_loot = {'sword': 1, 'apple': 1}
inventory.update(more_loot)
assert inventory.get('sword') == 2
# 使用Counter要注意的地方是：len只能返回其中unique元素的数量，而它的sum方法可以返回实际元素的数量
assert len(inventory) == 3
assert sum(inventory.values()) == 6
