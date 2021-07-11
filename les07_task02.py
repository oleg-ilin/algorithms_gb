"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


# код с википедии
def merge_sort(A):
    if len(A) == 1 or len(A) == 0:
        return
    L, R = A[:len(A) // 2], A[len(A) // 2:]
    merge_sort(L)
    merge_sort(R)
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(A)):
        A[i] = C[i]


print('Генерируем массив [0; 50), размер 10 элементов:')
array = []
while len(array) < 10:
    temp = random.random() * 50
    # значение 100 включать в список нельзя
    if temp != 50:
        array.append(temp)
print(array)
merge_sort(array)
print('Сортируем')
print(array)
