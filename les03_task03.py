"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

lst = [random.randint(1, 10) for el in range(6)]
print('Генерируем массив случайных чисел')
print(lst)
max = lst[0]
min = lst[0]
# max_index = 0  Инициализируем переменные, если используем в цикле
# min_index = 0
for i in lst:
    if i > max:
        max = i
        # max_index = (lst.index(i))   Можно определять min и max индексы в цикле
    elif i < min:
        min = i
        # min_index = (lst.index(i))
print(f'минимальное значение: {min}, максимальное значение: {max}')
min_index = lst.index(min)
max_index = lst.index(max)
lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
print('Меняем местами минимальное и максимальное значения')
print(lst)


