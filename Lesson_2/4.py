"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def n_sum(number):
    global a, b
    if number == 0:
        b = a
        return b
    else:
        b = b + a
        a = a / -2
        return n_sum(number - 1)


a = 1
b = 0
print(n_sum(int(input('Введите число элементов: '))))
