# -*- coding: utf-8 -*-
# Dilbert后面忘记加逗号,导致结果和预期的不符
names = [
    'Alice',
    'Bob',
    'Dilbert'
    'Jane'
]
print(f"bad practical:{names}")

# 好的写法
names = [
    'Alice',
    'Bob',
    'Dilbert',
    'Jane',
]
print(f"good practical:{names}")
