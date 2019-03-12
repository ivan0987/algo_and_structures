# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

#Схема на скриншоте 1.png

a = int(input('Введите трехзначное число: '))
my_sum = a % 10
my_prod = a % 10

a = a // 10

my_sum = my_sum + a % 10
my_prod = my_prod * a % 10

a = a // 10

my_sum = my_sum + a % 10
my_prod = my_prod * a % 10

print(my_sum, my_prod)