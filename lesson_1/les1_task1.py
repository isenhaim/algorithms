# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

print("Введите трехзначное чсисло:")
number = int(input())

num_1 = number // 100
num_2 = (number % 100) // 10
num_3 = (number % 100) % 10

sum_num = num_1 + num_2 + num_3
mult_num = num_1 * num_2 * num_3

print(f"Сумма цифр введенного числа: {sum_num}")
print(f"Произведение цифр введенного числа: {mult_num}")
