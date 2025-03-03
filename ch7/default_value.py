# -*- coding: utf-8 -*-
from asserts import assert_throw

# dict的get方法查找某个key对应的默认值，器第二个参数可以设置当找不到这个key的时候返回的默认值
name_for_userid = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert',
}


# 第一版实现，使用方括号来获取key对应的值
def greeting1(userid):
    return 'Hi %s!' % name_for_userid[userid]


# 当key找不到，这个实现会抛出异常
assert_throw(KeyError, lambda: greeting1(123))


# 第二版实现，先判断key是否在dict中，不再返回一个默认值
def greeting2(userid):
    if userid in name_for_userid:
        return 'Hi %s!' % name_for_userid[userid]
    else:
        return 'Hi there!'


assert greeting2(123) == 'Hi there!'


# 这个实现的问题是：
# 1.不高效，最差的情况会查询两次dict
# 2.两个分支返回的字符串的前半部分是重复的
# 3.不符合Python的“easier to ask for forgiveness than permission”(EAFP)编码风格

# 第三版，使用try-catch实现
def greeting3(userid):
    try:
        return 'Hi %s!' % name_for_userid[userid]
    except KeyError:
        return 'Hi there!'


assert greeting3(123) == 'Hi there!'


# 第四版，使用get
def greeting4(userid):
    return 'Hi %s!' % name_for_userid.get(userid, 'there')

assert greeting4(950) == "Hi Bob!"
assert greeting4(123) == "Hi there!"
