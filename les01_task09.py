'''
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
'''

print('Введите три разных числа')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if a > b:
    if a > c:
        if b > c:
            print(f'{b} - среднее число')
        else:
            print(f'{с} - среднее число')
    else:
        print(f'{a} - среднее число')
else:
    if b > c:
        if a > c:
            print(f'{a} - среднее число')
        else:
            print(f'{c} - среднее число')
    else:
        print(f'{b} - среднее число')

