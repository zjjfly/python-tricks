# -*- coding: utf-8 -*-

# 下面的表达式虽然简短，但解析的结果出乎意料
d = {True: 'yes', 1: 'no', 1.0: 'maybe'}
assert d == {True: 'maybe'}

# 把这个表达式分解成下面的代码
d = dict()
d[True] = 'yes'
d[1] = 'no'
d[1.0] = 'maybe'
# 这个dict的key在Python看来是相等的
assert True == 1 == 1.0
# 查看Python文档之后，发现bool类型实际是int类型的子类，False是0，True是1
# 所以下面的等式也是成立的
assert ['no', 'yes'][True] == 'yes'

# 所以实际上这个表达式更新了三次同一个key对应点值
# 但为什么最后的结果中的key不是1.0？这是因为dict在更新value的时候不会修改原来的key
ys = {1.0: 'no'}
ys[True] = 'yes'
assert ys == {1.0: 'yes'}


# 在dict中，实际上会对每个放入的key求hash值，根据hash值放在不同的桶中
# 所以，根本原因是True,1和1.0的算出的hash值是一样的
# 可以使用下面的类来测试dict到底是如何判断key是否相等的，是用对象的__eq__方法还是__hash__方法
# 这个类的__eq__用于返回的是True，但__hash__返回的是内存地址，所以永远不会和其他对象相同
class AlwaysEquals:
    def __eq__(self, other):
        return True

    def __hash__(self):
        return id(self)


assert len({AlwaysEquals(): 'yes', AlwaysEquals(): 'no'}.items()) == 2


# 可以看出对象的hash值不同可以防止被覆盖
# 再定义一个__hash__永远返回一个固定值的类
class SameHash:
    def __hash__(self):
        return 1


a = SameHash()
b = SameHash()
assert len({a: 'a', b: 'b'}.items()) == 2
# 可以看出单单只是hash值相同并不会被覆盖
# 所以，dict即会比较key的相等性，又会比较hash值来判断是否是同一个
# 刚刚已经验证了True，1和1.0的相等性，下面看它们的hash值是否相等
assert hash(True) == hash(1) == hash(1.0)
