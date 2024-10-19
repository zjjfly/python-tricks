# -*- coding: utf-8 -*-
import traceback


def assert_throw(exception_class, callable_):
    if callable(callable_):
        err = None
        try:
            callable_()
        except Exception as e:
            err = e
            if type(e) == exception_class:
                traceback.print_exception(e)
                return
        raise AssertionError(f"{exception_class.__name__} expected, but got {type(err).__name__}")
    else:
        raise ValueError(f"argument {callable_} is not a callable")


def comparable(cls):
    """ Class decorator providing generic comparison functionality """

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    cls.__eq__ = __eq__
    cls.__ne__ = __ne__
    return cls
