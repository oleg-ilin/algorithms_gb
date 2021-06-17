"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

print('Генерируем массив')
lst = [random.randint(1, 10) for el in range(6)]

print(lst)
max = lst[0]
min = lst[0]

for i in lst:
    if i > max:
        max = i
    elif i < min:
        min = i
print(f'минимальное значение: {min}, максимальное значение: {max}')
min_index = lst.index(min)
max_index = lst.index(max)
print(f'Позиция минимального: {min_index + 1}, позиция максимального: {max_index + 1}')
lst_02 = []

if lst[min_index + 1 : max_index :] != []:
    lst_02 = lst[min_index + 1:max_index:]
elif lst[min_index -1 : max_index: -1] != []:
    lst_02 = lst[max_index + 1:min_index:]
else:
    print('Между минимальным и максимальным элементов нет')

sum_ = 0
for el in lst_02:
    sum_ += el
print(f'Сумма элементов между минимальным и максимальным: {sum_}')