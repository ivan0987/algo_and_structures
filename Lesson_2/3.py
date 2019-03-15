"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

def my_sort(number):
    global rev_number
    if len(str(number)) == 1:
        return rev_number + str(number)
    else:
        rev_number = rev_number + str(number % 10)
        return my_sort(number // 10)


rev_number = ''
print(my_sort(int(input('Введите число: '))))
