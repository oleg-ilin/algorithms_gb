"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""

def sum_h(n):
    i = 1
    number = 1
    summ = 1
    while i != n:
        number /= 2
        number *= -1
        summ += number
        i += 1
    return summ

n = int(input('Введите количество элементов '))
print(sum_h(n))


# def sum_h(n):
#     if n == 1:
#         return 1
#     else:
#         summ = n + sum_h(n / 2 * -1)
    # i = 1
    # number = 1
    # summ = 1
    # while i != n:
    #     number /= 2
    #     number *= -1
    #     summ += number
    #     i += 1
    # return summ

# n = int(input('Введите количество элементов '))
# print(sum_h(n))

