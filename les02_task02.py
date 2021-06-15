"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

def even_odd(number: str) -> int:
    even = 0
    odd = 0
    for i in number:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

number = input('Введите число ')
even, odd = even_odd(number)
print(f'Четных: {even}, нечетных: {odd}')


# number = input('Введите число ')
# even = 0
# odd = 0
# for i in number:
#     if int(i) % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(f'Четных: {even}, нечетных: {odd}')


