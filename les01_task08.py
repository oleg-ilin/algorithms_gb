'''
Определить, является ли год, который ввел пользователем, високосным или невисокосным.
'''

year = int(input('Введите год :'))
a = year % 4
b = year % 100
c = year % 400
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} - високосный год')
        else:
            print(f'{year} - невисокосный год')
    else:
        print(f'{year} - високосный год')
else:
    print(f'{year} - невисокосный год')