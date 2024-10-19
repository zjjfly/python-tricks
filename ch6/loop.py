# -*- coding: utf-8 -*-

my_items = ['a', 'b', 'c']
# C背景的开发人员刚刚接触Python的时候，往往会这样迭代list
i = 0
while i < len(my_items):
    print(my_items[i])
    i += 1

# 首先把i相关的代码去掉，因为其容易引发错误，比如忘记在每次循环最后让i增加1，会导致无限循环
for i in range(len(my_items)):
    print(my_items[i])

# 但这样还是不够python，Python中最常用的方式应该是for-each语法
for item in my_items:
    print(item)

# 但如果你还是需要index的话，enumerate方法可以帮上忙
for i, item in enumerate(my_items):
    print(f'{i}: {item}')

emails = {
    'Bob': 'bob@example.com',
    'Alice': 'alice@example.com',
}

for name, email in emails.items():
    print(f'{name} -> {email}')

# 如果你的迭代要从index为a的元素开始，在index为n的时候结束，步长为s，还是可以使用range
my_items = ['a', 'b', 'c', 'd', 'e']
for i in range(1, len(my_items), 3):
    print(my_items[i])
