"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

import collections
import operator


class Leaf:

    def __init__(self, char: str, *value: int):
        if isinstance(char, tuple):
            self.char, self.value = char
        else:
            self.char = char
            self.value = value

    def __repr__(self):
        return f'Leaf: char "{self.char}" value {self.value}'


class Node:
    def __init__(self, value: int, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

    def __repr__(self):
        return f'Node: value "{self.value}" ' \
               f'left -> {self.left} ' \
               f'right -> {self.right}'


class Haffman:

    def __init__(self):
        self._code_table = {}

    def _get_table(self, tree, code=''):
        if isinstance(tree, Node):
            self._get_table(tree.left, code=f'{code}0')
            self._get_table(tree.right, code=f'{code}1')
        elif isinstance(tree, Leaf):
            self._code_table[tree.char] = code

    def encode(self, string, detail=False):
        """string encoding"""
        self._code_table = {}
        count = collections.Counter(string)
        array = collections.deque(map(Leaf, count.most_common()))
        if detail:
            print(array)

        # формируем дерево
        while len(array) > 1:
            sorted_array = sorted(array, key=operator.attrgetter('value'))
            array = collections.deque(sorted_array)
            leaf_small = array.popleft()
            leaf_bigger = array.popleft()
            node = Node(leaf_small.value + leaf_bigger.value,
                        leaf_small,
                        leaf_bigger)
            array.appendleft(node)

        tree = array.pop()
        if detail:
            print(tree)  # дерево Хаффмана

        self._get_table(tree)
        if detail:
            print(self._code_table)  # таблица кодирования.

        return ' '.join([self._code_table[char] for char in string])


if __name__ == '__main__':
    haf = Haffman()
    print(haf.encode('beep boop beer!'))

    print('*' * 50)
    # my_str = input('Введите строку для кодирования: ')
    my_str = 'beep boop beer!'
    print(haf.encode(my_str, detail=True))
