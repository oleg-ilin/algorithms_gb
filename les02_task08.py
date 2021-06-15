"""
Посчитать, сколько раз встречается определенная цифра во введенной последовательности чисел.
 Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

def dig_counter(sequence: str, dig: str) -> str:
    n = 0
    for i in sequence:
        if i == dig:
            n += 1
    return n

quant = int(input('Введите количество чисел '))

dig = input('Введите искомую цифру ')
full_sequence = ''
while quant  > 0:
    sequence = input('Введите последовательность чисел ')
    full_sequence += sequence
    quant -= 1
print(f'Искомая цифра в количестве: {dig_counter(full_sequence, dig)}')






