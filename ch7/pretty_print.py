# -*- coding: utf-8 -*-
import json

from common import assert_throw

# Python虽然为dict实现了__str__和__repr__方法，是它可以直接被打印出来，但也存在一些问题
# 首先，这个实现是单行的，没有换行和缩进，导致可读性很差，尤其是dict较复杂的时候
mapping= {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(mapping)
# {'a': 23, 'b': 42, 'c': 12648430}

# 一种替代是使用json.dumps来把dict转成json字符串再打印
print(json.dumps(mapping, indent=4, sort_keys=True))
# {
#     "a": 23,
#     "b": 42,
#     "c": 12648430
# }

# 但这种方式的也有局限性，它必须符合Json规范，即key必须是str类型或可以自动转成str的类型（int, float, bool or None）
assert_throw(TypeError,lambda: json.dumps({all: 'yup'}))

# 如果包含复杂类型，序列化也会失败
mapping['d']= {1, 2, 3}
assert_throw(TypeError,lambda: json.dumps(mapping))

# 有的时候你还无法把json.dumps的输出复制到代码中重建相同的dict
# Python中经典的方式来pretty print对象的方式是使用pprint模块
import pprint
pprint.pprint(mapping)
# {'a': 23, 'b': 42, 'c': 12648430, 'd': {1, 2, 3}}

