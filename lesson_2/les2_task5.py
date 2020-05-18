# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def sum_num(num):
    sum_digit = 0
    for i in num:
        sum_digit += int(i)
    return sum_digit, num


last_summary = 0
last_num = ''

while True:
    num = input('Введите натуральное число: ')

    if num.isdigit():
        sum_digit, num = sum_num(num)
        if sum_digit > last_summary:
            last_summary = sum_digit
            last_num = num
    else:
        break

print(f'Наибольшее по сумме цифр число {last_num} \nСумма его цифр равна: {last_summary}')
