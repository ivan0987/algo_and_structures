"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections


a = int(input('Введите число предприятий: '))
c = {}
for i in range(a):
    name = input(f'Введите наименование предприятия: ')
    first_p = int(input(f'Введите прибыль предприятия {name} за 1 квартал: '))
    second_p = int(input(f'Введите прибыль предприятия {name} за 2 квартал: '))
    third_p = int(input(f'Введите прибыль предприятия {name} за 3 квартал: '))
    fourth_p = int(input(f'Введите прибыль предприятия {name} за 4 квартал: '))
    summ = (first_p + second_p + third_p + fourth_p)
    b = collections.namedtuple('d', ['name', 'first_p', 'second_p', 'third_p', 'fourth_p', 'summ'])
    d = b(name=name, first_p=first_p, second_p=second_p, third_p=third_p, fourth_p=fourth_p, summ=summ)
    c[d.name] = {'first_p': d.first_p, 'second_p': d.second_p, 'third_p': d.third_p, 'fourth_p': d.fourth_p, 'summ': d.summ}
e = 0
j = 0
h = []
k = []
for i in c:
    f = c[i]
    j = j + f['summ']
print(f'Средняя прибыль составила {j / a} денег')
for i in c:
    f = c[i]
    if f['summ'] > (j / a):
        h.append(i)
    else:
        k.append(i)
print(f'Прибыль выше среднего: {h}')
print(f'Прибыль ниже среднего: {k}')


