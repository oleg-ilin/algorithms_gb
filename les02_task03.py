"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""

def func_reverse(number: list) -> str:
    copy_number = number.copy()
    reverse_number_str = ''
    for i in number:
        reverse_number_str += str(copy_number.pop())
    return reverse_number_str

number = list(input('Введите число '))
print(func_reverse(number))




# number = list(input('Введите число '))
# copy_number = number.copy()
# reverse_number_str = ''
# for i in number:
#     reverse_number_str += str(copy_number.pop())
# print(reverse_number_str)

