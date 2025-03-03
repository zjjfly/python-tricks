# -*- coding: utf-8 -*-

def comparable(cls):
    """ Class decorator providing generic comparison functionality """

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    cls.__eq__ = __eq__
    cls.__ne__ = __ne__
    return cls

def represent(cls):
    """ Class decorator providing generic represent functionality """

    def __repr__(self):
        args = []
        for (k, v) in self.__dict__.items():
            args.append(f'{k}={v!r}')
        s = ','.join(args)
        # !r在formatted string literal中的作用是使用对象的__repr__方法来表示对象
        return f'{self.__class__.__name__}({s})'

    cls.__repr__ = __repr__
    return cls
