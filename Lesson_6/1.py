"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
import sys
from memory_profiler import profile


# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# Вариант 1, оригинальный из 1 урока, обернут в функцию
@profile
def my_sum_1():
    a = 589  # int(input('Введите трехзначное число: '))
    my_sum = a % 10
    my_prod = a % 10

    a = a // 10

    my_sum = my_sum + (a % 10)
    my_prod = my_prod * (a % 10)

    a = a // 10

    my_sum = my_sum + (a % 10)
    my_prod = my_prod * (a % 10)

    print(my_sum, my_prod)  # Ссылок 22 и 0
    print(sys.getrefcount(a))   # Ссылок 65
    print(sys.getrefcount(my_sum))  # Ссылок 17
    print(sys.getrefcount(my_prod))  # Ссылок 3
    # 13.2 MiB     13.2 MiB   @profile


# Решение с использованием индексов:
@profile
def my_sum_2():
    a = '589'  # int(input('Введите трехзначное число: '))
    my_sum = int(a[0]) + int(a[1]) + int(a[2])
    my_prod = int(a[0]) * int(a[1]) * int(a[2])
    print(my_sum, my_prod)
    print(sys.getrefcount(a))   # Ссылок 5
    print(sys.getrefcount(my_sum))  # Ссылок 16
    print(sys.getrefcount(my_prod))  # Ссылок 3
    # 13.1 MiB     13.1 MiB   @profile


print(my_sum_1())
print(my_sum_2())

'''Итого: при использовании индексов количество ссылок на a сильно уменьшается. \
По объему же потребляемой памяти сильной разницы не заметно. Я пробовал увеличить длину числа до 34 символов - так же безрезультатно\
Python версии 3.7.2150, Windows 64-разрядная'''
