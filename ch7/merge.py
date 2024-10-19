# -*- coding: utf-8 -*-

# 有的时候需要把两个或多个dict合并为一个dict，如实现一个配置系统

xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}

# 最简单的方式合并dict的方式是调用dict的update方法，如果传入的dict中相同的key的话会覆盖
zs = {}
zs.update(xs)
zs.update(ys)
assert zs == {'a': 1, 'b': 3, 'c': 4}

# 可以多层嵌套update函数来合并多个dict，这是一个实用和可读性很强的方案，且兼容Python2和3
# 另一个兼容Python2和3的方案是使用dict构造器和**操作符
zs = dict(xs, **ys)
assert zs == {'a': 1, 'b': 3, 'c': 4}

# 和update一样，这个方案只能合并两个dict，且无法像update一样串联来合并任意多个dict
# Python3.5之后，**操作符变得更加灵活，所以有一个新的方案可以使用了
zs = {**xs, **ys}
assert zs == {'a': 1, 'b': 3, 'c': 4}

# 在Python3.9中，操作符|也可以合并dict了
zs = xs | ys
assert zs == {'a': 1, 'b': 3, 'c': 4}

# 就个人来说，如果使用的是较新版本的Python，更倾向于使用最后一种方式，这种方式的可读性和简洁性都是最好的
# 如果考虑兼容性，可以使用update
