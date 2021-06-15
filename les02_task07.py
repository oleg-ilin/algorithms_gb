"""
Напишите программу, доказывающую или проверяющую, что для множества натуральных
чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""

# Рекурсивная функция
def sum_n(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n + sum_n(n - 1)

n = int(input('Введите число n '))
sum_f = int(n * (n + 1) / 2)
print(f'1 + 2 + ... + n = {sum_n(n)}')
print(f'n * (n + 1) / 2 = {sum_f}')


# def sum_n(n: int) -> int:
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i
#     return sum
#
# n = int(input('Введите число n '))
# sum_f = int(n * (n + 1) / 2)
# print(f'1 + 2 + ... + n = {sum_n(n)}')
# print(f'n * (n + 1) / 2 = {sum_f}')


# n = int(input('Введите число n '))
# summ_01 = 0
# for i in range(1, n + 1):
#     summ_01 += i
# summ_02 = int(n * (n + 1) / 2)
# print(f'1 + 2 + ... + n = {summ_01}')
# print(f'n * (n + 1) / 2 = {summ_02}')




