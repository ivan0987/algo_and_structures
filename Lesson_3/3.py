#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

# Массив возьму из прошлой задачи

a = [8, 16, 15, 6, 4, 2]
max = a[0]
min = a[0]
c = 0
d = 0
e = 0
for i in a:
    if i > max:
        max = i
        d = c
        c += 1
    elif i < min:
        min = i
        e = c
        c += 1
    else:
        c += 1

a.insert(e, max)
a.pop(e + 1)
a.insert(d, min)
a.pop(d + 1)

print(a)
