# -*- coding: utf-8 -*-
import asserts


# 尽量使用自定义的错误类型，而不是内置的那些较为宽泛的错误类型

class NameTooShortError(ValueError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)
    print(name)


common.assert_throw(NameTooShortError, lambda: validate('xyz'))


# 如果代码会被发布或被其他模块复用，那么需要定义一个基础的自定义错误类，其他的自定义错误类都从这个类派生
class BaseValidationError(ValueError):
    pass


class NameTooShortError(BaseValidationError):
    pass


class NameTooLongError(BaseValidationError):
    pass


class NameTooCuteError(BaseValidationError):
    pass
