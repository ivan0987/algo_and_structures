"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
import random, timeit


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(list):
    if len(list) < 2:
        return list
    middle = int(len(list) / 2)
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    return merge(left, right)


my_list = [random.randint(-100, 100) for i in range(10)]
print('Исходный список: ', my_list)
print('Отсортированный список: ', merge_sort(my_list))
print('Затраченое время: ', timeit.timeit('merge_sort(my_list)', setup='from __main__ import merge_sort, my_list', number=1))
