# -*- coding: utf-8 -*-

# 在调用函数的时候，把*放在一个iterable参数之前，可以对其进行unpack，把其中的每一个元素变为传入函数的一个positional argument
def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))


tuple_vec = (1, 0, 1)
print_vector(*tuple_vec)
# <1, 0, 1>


# 这也适用于generator expression
genexpr = (x * x for x in range(3))
print_vector(*genexpr)
# <0, 1, 4>


# **是对于dictionary进行unpack，
# 由于dict是无序的，所以会使用dict的key和函数的参数名进行匹配找到对应的值，再传入函数
dict_vec = {'y': 0, 'z': 1, 'x': 1}
print_vector(**dict_vec)
# <1, 0, 1>

# 如果使用*代替**来unpack，则会传入dict的keys，以任意顺序
print_vector(*dict_vec)
# <y, z, x>
