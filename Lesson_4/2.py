import timeit
"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

#Без решета
a = int(input('Введите номер простого числа: '))
print(timeit.timeit(stmt='''\
lst = []
b = 2
c = 0
while len(lst) < a:
    for i in range(2, b):
        if b % i == 0:
            c = c + 1
    if c == 0:
        lst.append(b)
        c = 0
    else:
        c = 0
    b += 1
print(lst[-1])''', setup='from __main__ import a', number=1))
# Результат: 7.087999999999539e-05

#С решетом
aa = int(input('Введите номер простого числа: '))
b = int(input('Введите количество чисел: '))
print(timeit.timeit(stmt='''\
lst = [i for i in range(b)]
lst = lst[2:]
for i in lst:
    for j in lst:
        if j == i:
            continue
        if j % i == 0:
            lst.remove(j)
print(lst[aa - 1])''', setup='from __main__ import aa, b', number=1))
# Результат: 0.0015615990000004132


