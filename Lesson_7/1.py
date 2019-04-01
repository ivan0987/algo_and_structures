"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import timeit
import random


def bubble_sort(list):
    n = 1
    while n < len(list):
        for i in range(len(list)-n):
            if list[i] < list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
        n += 1
    return list


def shake_sort(list):  # добавлено перемешивание
    n = 1
    m = len(list) - 1
    while n < (len(list) / 2):
        for i in range(len(list)-n):
            if list[i] < list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
            if list[m] > list[m-1]:
                list[m], list[m-1] = list[m-1], list[m]
        n += 1
        m -= 1
    return list

my_list = [random.randint(-100, 100) for i in range(10)]
print('Исходный список: ', my_list)
print('Отсортированный список Пузырьки: ', bubble_sort(my_list))
print('Отсортированный список Шейкер: ', shake_sort(my_list))
print('Затраченое время Пузырьки: ', timeit.timeit('bubble_sort(my_list)', setup='from __main__ import bubble_sort, my_list', number=1))
print('Затраченое время Шейкер: ', timeit.timeit('shake_sort(my_list)', setup='from __main__ import shake_sort, my_list', number=1))

