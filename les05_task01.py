"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
 для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
  отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

#Вариант  с defaultdict

import collections

quantity = int(input('Введите кол-во компаний: '))
companies = {}
companies_profit = collections.defaultdict(list)
for n in range(0, quantity):
    companies[n] = input(f'Введите название компании {n + 1}: ')
    for k in range(1, 5):
        quarter = (companies[n], float(input(f'Введите размер прибыли компании {companies[n]} за {k} квартал: ')))
        companies_profit[companies[n]].append(quarter[1])
print('*********************************************************')

common_profit = 0
for key, value in companies_profit.items():
    common_profit += sum(value)
print(f'Общая прибыль компаний: {round(common_profit, 2)}')
avrg_profit = common_profit / quantity
print(f'Средняя прибыль компаний: {round(avrg_profit, 2)}')

low_level = []
high_level = []
avrg_level = []

for key, value in companies_profit.items():
    if sum(value) < avrg_profit:
        low_level.append(key)
    elif sum(value) > avrg_profit:
        high_level.append(key)
    else:
        avrg_level.append(key)

print('Компании с уровнем прибыли ниже среднего: ')
for i in low_level:
    print(i)
print('Компании с уровнем прибыли выше среднего: ')
for i in high_level:
    print(i)
print('Компании с уровнем прибыли равном среднему: ')
if avrg_level == []:
    print('Не имеется')
else:
    for i in avrg_level:
        print(i)


#Вариант с setdefault

quantity = int(input('Введите кол-во компаний: '))
companies = {}
companies_profit ={}
for n in range(0, quantity):
    companies[n] = input(f'Введите название компании {n + 1}: ')
    for k in range(1, 5):
        quarter = float(input(f'Введите размер прибыли компании {companies[n]} за {k} квартал: '))
        companies_profit.setdefault(companies[n], []).append(quarter)
print('******************************************************')

common_profit = 0
for key, value in companies_profit.items():
    common_profit += sum(value)
print(f'Общая прибыль компаний: {round(common_profit, 2)}')
avrg_profit = common_profit / quantity
print(f'Средняя прибыль компаний: {round(avrg_profit, 2)}')

low_level = []
high_level = []
avrg_level = []

for key, value in companies_profit.items():
    if sum(value) < avrg_profit:
        low_level.append(key)
    elif sum(value) > avrg_profit:
        high_level.append(key)
    else:
        avrg_level.append(key)

print('Компании с уровнем прибыли ниже среднего: ')
for i in low_level:
    print(i)
print('Компании с уровнем прибыли выше среднего: ')
for i in high_level:
    print(i)
print('Компании с уровнем прибыли равном среднему: ')
if avrg_level == []:
    print('Не имеется')
else:
    for i in avrg_level:
        print(i)


