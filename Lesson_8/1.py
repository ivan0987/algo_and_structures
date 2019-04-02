"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

''' Возьмем строку 'back land man' 
Построим таблицу и отсортируем:
b   | 1
c   | 1
k   | 1
l   | 1
m   | 1
' ' | 2
n   | 2
d   | 2
a   | 3

Построим дерево:
                                 _________0__________14__________1_________
                                /                                          \                 
                         ___0__6___1___                                ______0__8__1______
                        /              \                             /                     \ 
                    _0_3_1_          ___a___                     _0_4_1_                 _0_4_1_
                   /       \                                    /       \               /       \ 
                 _k_     _0_2_1_                               _' '_     _0_2_1_       _n_      _d_     
                        /       \                                       /       \ 
                       _b_      _c_                                   _l_       _m_


b   | 0010
c   | 0011
k   | 000
l   | 1010
m   | 1011
' ' | 100
n   | 110
d   | 111
a   | 01

Таким образом: 
'back land man'
0010 01 0011 000 100 1010 01 110 111 100 1011 01 110
'''

import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def main():
    s = input('Введите строку для кодирования: ')
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)


if __name__ == "__main__":
    main()
