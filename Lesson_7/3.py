"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
from statistics import median
import random, timeit


def my_median(list):
    n = 1
    while n < (len(list) / 2) + 1:
        for i in range(len(list)-n):
            if list[i] < list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
        n += 1
    return list[n - 2]


my_list = [random.randint(-100, 100) for i in range(11)]
print('Исходный список: ', my_list)
print('Медиана через стандартный statistics.median: ', median(my_list))
print('Медиана своя: ', my_median(my_list))
print('Затраченое время: ', timeit.timeit('my_median(my_list)', setup='from __main__ import my_median, my_list', number=1))
