# -*- coding: utf-8 -*-
from string import Template

errno = 50159747054
name = 'Bob'
target = 'Hey Bob, there is a 0xbadc0ffee error!'

# old style
s = 'Hello,%s' % name
assert 'Hello,Bob' == s

n = '%x' % errno
assert 'badc0ffee' == n

s1 = 'Hey %s, there is a 0x%x error!' % (name, errno)
assert target == s1

s2 = 'Hey %(name)s, there is a 0x%(errno)x error!' % {"name": name, "errno": errno}
assert target == s2

# new style(Python 3)
s = 'Hello,{}'.format(name)
assert 'Hello,Bob' == s

# 可以在花括号中加上具体的参数名，并使用带名参数。
# 相比上面的那种方式，当要对参数在字符串中的占位符位置进行修改，就不需要修改传入的参数顺序了
s1 = 'Hey {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno)
assert target == s1

# formatted string literals(Python3.6+)，这实际是一个语法糖，底层是通过parser把它转成多个子字符串和表达式然后拼装起来
s = f'Hello,{name}'
assert 'Hello,Bob' == s
a = 5
b = 10
s = f'Five plus ten is {a + b} and not {2 * (a + b)}.'
assert 'Five plus ten is 15 and not 30.' == s

s1 = f"Hey {name}, there is a {errno:#x} error!"
assert target == s1

# Template String，一般用于当需要用户提供需要format的字符串的时候，它相比其他方案更安全，也更简单
t = Template('Hello,$name')
s = t.substitute(name=name)
assert 'Hello,Bob' == s

templ_string = 'Hey $name, there is a $error error!'
s1 = Template(templ_string).substitute(name=name, error=hex(errno))
assert target == s1

SECRET = 'this-is-a-secret'


class Error:
    def __init__(self):
        pass


err = Error()
user_input = '{error.__init__.__globals__[SECRET]}'
# 下面的代码可以打印出SECRET，这是很致命的安全问题
s = user_input.format(error=err)
assert 'this-is-a-secret' == s

user_input = '${error.__init__.__globals__[SECRET]}'
try:
    Template(user_input).substitute(error=err)
except ValueError as e:
    err = e
assert err

# 选择格式化字符串方式的原则：
# 如果是用户输入的字符串，则使用template string
# 否则，使用3.6引入的formatted string literal
