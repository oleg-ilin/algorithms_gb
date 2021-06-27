"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

def func(num, mem):
    for el in range(0, len(num)):
        num_temp = num.pop()
        sum_temp = my_dict[num_temp] + mem
        if sum_temp > 15:
            sum_temp -= 16
            mem = 1
            res.append(sum_temp)
        else:
            res.append(sum_temp)
            mem = 0
    if mem == 1:
        res.append(mem)
    return res

def func_res_16(res):
    res = res[::-1]
    res_16 = []
    for el in res:
        for key, value in my_dict.items():
            if el == value:
                res_16.append(key)
    return res_16


print('Сложение шестнадцатеричных чисел')

num_01 = list(input('Введите первое число в любом регистре: ').upper())
print(num_01)
num_02 = list(input('Введите второе число: ').upper())
print(num_02)

res = []
temp = 0
my_dict = {'0' : 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
           }

sum_ = 0
mem = 0
while num_01 != [] and num_02 != []:
    num_temp_01 = num_01.pop()
    num_temp_02 = num_02.pop()
    sum_temp = my_dict[num_temp_01] + my_dict[num_temp_02] + mem
    if sum_temp > 15:
        sum_temp -= 16
        mem = 1
        res.append(sum_temp)
    else:
        res.append(sum_temp)
        mem = 0

if num_01 == [] and num_02 == []:
    if mem == 1:
        res.append(mem)
    res = func_res_16(res)

elif num_01 == []:
    res = func(num_02, mem)
    res = func_res_16(res)

else:
    res = func(num_01, mem)
    res = func_res_16(res)

print(f'Ответ:', ''.join(res))
