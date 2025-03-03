# -*- coding: utf-8 -*-
from asserts import assert_throw

# Array是大多数编程语言的基础程序结构，它在相邻的内存中存储数据，并可以通过index方法其中的元素，
# Python中的几种Array实现：

# list，Python语言核心的一部分。它是通过dynamic array实现的，这意味着它可以动态的改变其长度
# 它可以存放任意类型的值，但这样的缺点是结构不紧凑，会占用较多的内存
arr = ['one', 'two', 'three']
assert arr[0] == 'one'
# list是可变的
arr[1] = 'hello'
assert arr[1] == 'hello'
del arr[1]
assert len(arr) == 2
arr.append(23)
assert len(arr) == 3
assert arr[2] == 23

# tuple，和list类似，它也是Python语言核心的一部分，但和list不同的是，它是不可变的
# 它也可以存放任意类型的值，所以从内存角度来看也不是很紧凑
arr = 'one', 'two', 'three'
assert arr[0] == 'one'
# tuple是不可变的，所以无法更改或删除其中的元素
try:
    arr[1] = 'hello'
    assert False
except TypeError as e:
    print(e)
try:
    del arr[1]
    assert False
except TypeError as e:
    print(e)
# tuple可以使用+操作符来添加元素，但返回的是新的tuple
arr1 = arr + (23,)
assert arr1 == ('one', 'two', 'three', 23)
# tuple在内存利用和构造速度上高于list，但可以忽略不计
# 使用dis来看它们构造使用的指令，tuple的明显较少
from dis import dis

dis(compile("(23, 'a', 'b', 'c')", '', 'eval'))
#   1           2 RETURN_CONST             0 ((23, 'a', 'b', 'c'))
#   0           0 RESUME                   0
dis(compile("[23, 'a', 'b', 'c']", '', 'eval'))
#   1           2 BUILD_LIST               0
#               4 LOAD_CONST               0 ((23, 'a', 'b', 'c'))
#               6 LIST_EXTEND              1
#               8 RETURN_VALUE

# array.array，它是一个typed array，即存储的元素类型必须是一致的
# 所以它是比较紧凑的数据结构，可以节省内存空间
# 它支持很多和list相同的方法，所以一般可以直接替换
from array import array

arr = array('f', (1.0, 1.5, 2.0, 2.5))
assert arr[1] == 1.5
# 它有一个漂亮的repr实现
print(arr)
# 它是可变的
arr[1] = 23.0
assert arr[1] == 23.0
del arr[1]
assert len(arr) == 3
arr.append(42.0)
assert len(arr) == 4
assert arr[3] == 42.0
# 改变其中的元素为其他类型的值会报错
try:
    arr[1] = 'hello'
    assert False
except TypeError as e:
    print(e)

# str，即字符串类型，它实际是一个不可变的unicode字符数组
# 怪异的是，它是一个递归的数据结构，数组中的每一个unicode字符实际是长度为1的str对象
# 它也是一个紧凑的数据结构，因为其中存储的值的类型是一致的
# 它是不可变的，所以对其的修改会产生一个新的str
arr = 'abcd'
assert arr[1] == 'b'
try:
    arr[1] = 'e'
    assert False
except TypeError as e:
    print(e)
try:
    del arr[1]
    assert False
except TypeError as e:
    print(e)
# 可以使用把str中的拆接出来放入list来获得一个可变的unicode字符数组
unicode_list = list('abcd')
# 使用join再转回str
assert ''.join(list('abcd')) == 'abcd'
# 下面的代码可以验证它是一个递归的数据结构
assert type('abc') == str
assert type('abc'[0]) == str

# bytes，不可变的字节数组，实际是一个不可变的int类型的数组
arr = bytes((0, 1, 2, 3))
assert arr[1] == 1
# bytes有字面量语法
arr = b'x00x01x02x03'
# 它要求其中的元素在 0~255 范围内，如不符合要求则会报错
assert_throw(ValueError, lambda: bytes((0, 300)))
# ValueError: bytes must be in range(0, 256)

# bytearray，可变的字节数组
arr = bytearray((0, 1, 2, 3))
assert arr[1] == 1
arr[1] = 23
assert arr[1] == 23
del arr[1]
assert len(arr) == 3
arr.append(42)
assert arr[3] == 42
# 可以把bytearray转成bytes
assert bytes(arr) == bytes((0, 2, 3, 42))
