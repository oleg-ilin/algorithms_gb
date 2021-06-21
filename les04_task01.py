"""
Определить, какое число в массиве встречается чаще всего.
"""

import random
import cProfile
from timeit import timeit

START = 1
STOP = 1000
RANGE_ = 3000

lst = [random.randint(START, STOP) for el in range(RANGE_)]


# Вариант 1
def more_frequently_01(lst: list) -> int:
    # print(lst)
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
    return element, max_count


# ваниант преподавателя со словарём
def more_frequently_02(lst: list) -> int:
    counter = {}
    frequency = 1
    num = None
    for item in lst:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

        if counter[item] > frequency:
            frequency = counter[item]
            num = item

    if num is not None:
        return num, frequency

    else:
        print('Все элементы уникальны')


# Вариант 3 с доп. циклом
def more_frequently_03(lst: list) -> int:
    test = 0
    element = 0
    max_count = 0
    for el in lst:
        count = 0
        for i in lst:
            if el == i:
                count += 1
                for k in lst:  # Дополнительный тестовый цикл для увеличения сложности
                    test += k
            if count > max_count:
                max_count = count
                element = el
    return element, max_count


element, max_count = more_frequently_01(lst)
print(f'Число {element} встречается чаще других. А именно {max_count} раз(а)')

element, max_count = more_frequently_02(lst)
print(f'Число {element} встречается чаще других. А именно {max_count} раз(а)')

element, max_count = more_frequently_03(lst)
print(f'Число {element} встречается чаще других. А именно {max_count} раз(а)')

cProfile.run('more_frequently_01(lst)')
cProfile.run('more_frequently_02(lst)')
cProfile.run('more_frequently_03(lst)')

for i in range(3):
    print(timeit(f'more_frequently_01({lst})', number=5, globals=globals()))
print()
for i in range(3):
    print(timeit(f'more_frequently_02({lst})', number=5, globals=globals()))
print()
for i in range(3):
    print(timeit(f'more_frequently_03({lst})', number=5, globals=globals()))

"""
4 function calls in 0.429 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.429    0.429 <string>:1(<module>)
        1    0.429    0.429    0.429    0.429 les04_task01.py:17(more_frequently_01)
        1    0.000    0.000    0.429    0.429 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
        
4 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 les04_task01.py:33(more_frequently_02)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
        
4 function calls in 3.537 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.537    3.537 <string>:1(<module>)
        1    3.537    3.537    3.537    3.537 les04_task01.py:55(more_frequently_03)
        1    0.000    0.000    3.537    3.537 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
        
2.1709869420000008
2.196539046
2.166255054999999

0.0044812420000006625
0.004660884999999837
0.004541978000000668

17.415361116999996
17.694311470000002
17.485133243999996

Вывод:
Время выполнения функций сильно отличается в соответствии с их сложностью.
Сложность функции more_frequently_01 квадратичная - O(n^2). Есть внешний цикл, который повторяет 
все элементы во входном списке, а затем вложенный внутренний цикл, который снова повторяет 
все элементы во входном списке. 
Сложность функции more_frequently_02 линейна - O(n), так как число итераций цикла for  
равно размеру входного элемента массива, по-этому функция самая быстрая из трех.
Функция more_frequently_03 является кубической - O(n^3), так как в уже вложенный цикл также добавлен 
еще один вложенный цикл, что безусловно превращает функцию в самую медленную из представленных.

"""
