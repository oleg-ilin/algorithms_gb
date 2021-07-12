"""
 Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
 состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""

import itertools
import lorem
from pprint import pprint
from timeit import timeit
from string import ascii_lowercase

data = 'abcd'
res_set_ = set()


def timeit_(func1, func2, max_=8):
    print('\n'*2)
    print('-'*44)
    print(f'{func1:-<20} VS {func2:->20}')
    print('-'*44)
    for i in range(2, max_):
        data = ascii_lowercase[:i]
        a = timeit(f'{func1}("{data}")', number=100, globals=globals())
        b = timeit(f'{func2}("{data}")', number=100, globals=globals())
        print(f'{data:-<16}, {a:.7f}, {b:.7f}')

# -----------------------------------------------------------------------------
def tree_permutations(val, res=''):
    res_set_.add(res)
    for i, letter in enumerate(val):
        new_val = val[:i] + val[i + 1:]
        tree_permutations(new_val, res + letter)


def permutations_(val):
    res_set = set()
    for L in range(len(val) + 1):
        for subset in itertools.permutations(val, L):
            res = ''.join(subset)
            res_set.add(res)

    return res_set

timeit_('permutations_', 'tree_permutations', 8)

res_set2 = permutations_(data)
res_set_ = set()
tree_permutations(data)
pprint(f'{res_set_} {"-"*100} уникальных строк: {len(res_set_) - 2}')
pprint(f'{res_set2} {"-"*100} уникальных строк: {len(res_set2) - 2}')