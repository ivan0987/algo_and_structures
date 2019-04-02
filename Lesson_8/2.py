"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib


str_in = input('Введите строку, состоящую только из маленьких латинских букв: ').encode('utf-8')
substr = set()
for i in range(len(str_in)):
    if i == 0:
        n = len(str_in) - 1
    else:
        n = len(str_in)
    for j in range(n, i, -1):
        substr.add(hashlib.sha1(str_in[i:j]).digest())
print(substr)
print('Количество различных подстрок в строке: ', len(substr))
