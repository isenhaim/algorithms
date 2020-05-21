# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

min_num = array[0]
max_num = array[0]

for i in array:
    if i < min_num:
        min_num = i
    if i > max_num:
        max_num = i

print(f'Исходный массив: {array}')
array[array.index(min_num)], array[array.index(max_num)] = array[array.index(max_num)], array[array.index(min_num)]

print(f'Максимальный элемент: {max_num} \nМинимальный элемент: {min_num}')
print(f'Массив с взаимозаменеными элементами: {array}')
