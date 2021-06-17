"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

lst = [random.randint(1, 10) for el in range(10)]
print(lst)
element = 0
max_count = 0
for el in lst:
    count = 0
    for i in lst:
        if el == i:
            count += 1
    if count > max_count:
        max_count = count
        element = el
print(f'Число {element} встречается чаще других. А именно {max_count} раз')
