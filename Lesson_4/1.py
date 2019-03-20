import timeit
import cProfile
"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
# Мой алгоритм


def my():
    a = 1860
    if a % 400 == 0:
        print('Високосный')
    elif a % 4 == 0:
        if a % 100 != 0:
            print('Високосный')
        else:
            print('Не високосный')
    else:
        print('Не високосный')


print(timeit.timeit('my()', setup='from __main__ import my', number=10))
cProfile.run('my()')
# Результат: 8.88410000000027e-05
'''         5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 1.py:11(my)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''


def my1():
    a = 1860
    if a % 4 != 0 or (a % 100 == 0 and a % 400 != 0):
        print("Не високосный")
    else:
        print("Високосный")


print(timeit.timeit(stmt='my1()', setup='from __main__ import my1', number=10))
cProfile.run('my1()')
# Результат: 7.023800000000024e-05
'''         5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 1.py:39(my1)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''

'''Вывод. 
    1. Профилирование в данном примере бесполезно. По результатам применения timeit могу предположить, 
    что причиной разницы в скорости является меньшая цикломатическаю сложность второго алгоритма'''







