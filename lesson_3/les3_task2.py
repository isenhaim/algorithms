# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
import random

SIZE = 100000
MIN_ITEM = 0
MAX_ITEM = 100000

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
result_list = []

for i in range(len(array)):
    result_list.append(i) if array[i] % 2 == 0 else None

print(f'Исходный массив: {array}')
print(f'Массив с позициями четных чисел: {result_list}')
