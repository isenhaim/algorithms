# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

num_1 = input('Введите 1-е шестнадцатеричное число: ')
num_2 = input('Введите 2-е шестнадцатеричное число: ')

dec = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
    'D': 13, 'E': 14, 'F': 15
}

# num_1 = 'A2'
# num_2 = 'C45'
# num_1 = 'A4111AA'
# num_2 = 'E133E'

def get_key(dic, num):
    for key in dic.keys():
        if num == dec.get(key):
            return key
        pass


num_1 = deque([i.upper() for i in num_1])
num_2 = deque([i.upper() for i in num_2])

num_1.reverse()
num_2.reverse()

k = 0
result = deque()
max_len = len(num_2) if len(num_2) > len(num_1) else len(num_1)

for i in range(max_len):
    try:
        sum_ = int(dec.get(num_1[i])) + int(dec.get(num_2[i])) + k
        k = 0

        if sum_ > 16:
            r = sum_ - 16
            result.append(get_key(dec, r))
            k += 1

            if i == max_len - 1:
                result.append(k)

        for key in dec.keys():
            if sum_ == dec.get(key):
                result.append(key)

    except IndexError:
        last_num = num_1[i] if len(num_1) == max_len else num_2[i]
        result.append(last_num)


result.reverse()
print(f'Результат сложения: {"".join(map(str, result))}')
