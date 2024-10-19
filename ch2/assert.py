# -*- coding: utf-8 -*-
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 < price < product['price']
    return price


shoes = {'name': 'Fancy Shoes', 'price': 14900}
assert 11175 == apply_discount(shoes, 0.25)

# 不要用assert做数据验证
# def delete_product(prod_id, user):
#     assert user.is_admin(), 'Must be admin'
#     assert store.has_product(prod_id), 'Unknown product'
#     store.get_product(prod_id).delete()

# assert后面的表达式不能加括号
# 下面的代码会报错,因为编译器发现assert后面的表达式用于是true
# assert (1 == 2, 'This should fail')
# 如果你想要抛出AssertionError的时候打印自定义信息,使用下面这种写法
assert 1 == 2, "This should fail"
