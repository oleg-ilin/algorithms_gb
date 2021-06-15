"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""


def sum_h_r(n, i=1, number=1, summ=1):
    if i == n:
        return summ
    else:
        number /= 2
        number *= -1
        summ += number
        i += 1
        return sum_h_r(n, i, number, summ)


n = int(input('Введите количество элементов '))
print(sum_h_r(n))


