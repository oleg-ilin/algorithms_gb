"""
В одномерном массиве целых чисел определить два наименьших элемента.
 Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random

print('Генерируем массив')
lst = [random.randint(1, 10) for el in range(6)]
print(lst)
min_index_01 = 0
min_01 = lst[0]

for i in lst:                #Находим первое мин
    if i < min_01:
        min_01 = i
        min_index_01 = lst.index(min_01)

min_02 = lst[0] if min_index_01 != 0 else lst[1]  #Второе мин. начинается с инд. 0, если не занято первым мин.
count = 0

for k in lst:                                   #Находим второе мин
    if k < min_02 and min_index_01 != count:
        min_02 = k
    count += 1

print(f'Первое наименьшее число: {min_01}\nВторое наименьшее число: {min_02}')
