'''
По длинам трех отрезков, введенных пользователем, определить возможность существования
треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить,
является ли он разносторонним, равнобедренным или равносторонним.
'''

a = int(input('Введите длину первой стороны треугольника '))
b = int(input('Введите длину второй стороны треугольника '))
c = int(input('Введите длину третьей стороны треугольника '))
if a + b > c and a + c > b and b + c > a:
    if a != b and a != c and b != c:
        print('Треугольник разносторонний')
    else:
        if a == b and a == c and b == c:
            print('Треугольник равносторонний')
        else:
            print('Треугольник равнобедренный')
else:
    print('Треугольник не существует')

