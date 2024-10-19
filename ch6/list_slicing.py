# -*- coding: utf-8 -*-

# Python的list有一个巧妙的功能叫slicing，你可以把它看成是对方括号索引语法的扩展
# 它一般用于取list的其中某一段范围的内容，它的语法是[start:stop:step]
# start默认是0，stop默认是list的长度，step默认也是1
lst = [1, 2, 3, 4, 5]
assert lst[1:3:1] == [2, 3]

# 为了防止索引超出，要记住stop对应的元素是exclusive的
# step可以省略
assert lst[1:3] == [2, 3]
# step可以是负数，下面这个例子就是用-1的step来reverse一个list（但最好还是使用list的reverse方法或reversed方法来实现，为了可读性）
assert lst[::-1] == [5, 4, 3, 2, 1]

# 还可以使用slicing来清空一个list，因为有的时候用一个新的list对象来替换原来的会有问题
del lst[:]
assert lst == []
# 当然，在Python3中，list加入了clear方法，这种方式更有可读性
lst = [1, 2, 3, 4, 5]
lst.clear()
assert lst == []

# 可以使用它来替换lis中所有的元素而保持原来的对象
original_lst= lst
lst[:]= [7, 8, 9]
assert lst == [7, 8, 9]
assert original_lst == [7, 8, 9]

# 还可以使用它来复制list（浅拷贝）
copied_lst= lst[:]
assert copied_lst == [7, 8, 9]
# 复制的list和原来的list不是一个对象
assert copied_lst is not lst

#
