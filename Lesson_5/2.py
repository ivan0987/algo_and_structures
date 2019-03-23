"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

# тут у меня упорно не сходятся результаты, что в 1 случае, что во втором. Во втором - уж очень сильно
import collections


def summ(b, c, dic):
    d = 0
    f = 0
    h = 0
    g = []
    for i in range(len(b)):
        d = int(my_dic.get(b[i])) + int(my_dic.get(c[i])) + h
        h = 0
        if d > 16:
            f = d % 16
            h = d // 16
            g.append(f)
        else:
            g.append(d)
    if h > 0:
        g.append(h)
    g.reverse()
    return g


def prod(b, c, dic):
    d = 0
    f = 0
    h = 0
    t = 0
    g = []
    for i in range(len(b)):
        d = int(my_dic.get(b[i])) * int(my_dic.get(c[i])) + h
        h = 0
        if d > 16:
            f = d % 16
            h = d // 16
            g.append(f)
            if h > 16:
                t = h // 16
                h = h % 16
                g.append(t)
        else:
            g.append(d)
    if h > 0:
        g.append(h)
    g.reverse()
    return g


def ten_to_sixteen(g, my_rev_dic):
    h = []
    for i in g:
        h.append(my_rev_dic.get(str(i)))
    return h


my_dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 14, 'E': 15, 'F': 16}
my_rev_dic = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': 'A', '11': 'B', '12': 'C', '14': 'D', '15': 'E', '16': 'F'}
a = input('Введите требуемую операцию: + или *: ')
b = list(input('Введите первое шестнадцатеричное число: '))
c = list(input('Введите второе шестнадцатеричное число: '))
b.reverse()
c.reverse()
m = ''
if len(b) > len(c):
    for i in range(len(b) - len(c)):
        c.append('0')
elif len(c) > len(b):
    for i in range(len(c) - len(b)):
        b.append('0')

if a == '+':
    a = ten_to_sixteen(summ(b, c, my_dic), my_rev_dic)
    for i in a:
        m += i
    print(m)
elif a == '*':
    a = ten_to_sixteen(prod(b, c, my_dic), my_rev_dic)
    for i in a:
        m += i
    print(m)
else:
    print('Неверная операция')




