# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint

# Беру матрицу 5х5
min = 10  # Минимальное по столбцу
max = 0 # Максимальное среди минимальных
a = []
b = []
for i in range(5):
    for j in range(5):
        b.append(randint(0, 10))
        for k in b:
            if k < min:
                min = k
    if min > max:
        max = min
    min = 10
    a.append(b)
    b = []

print(a)
print(max)
