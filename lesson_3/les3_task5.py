# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random

SIZE = 100000
MIN_ITEM = -70
MAX_ITEM = -5

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_negative = array[0]

for i in array:
    if max_negative > i:
        max_negative = i

for i in array:
    if i < 0:
        if max_negative < i:
            max_negative = i



print(f'Исходный массив: {array}')
print(f'Максимальное отрицательное число в массиве: {max_negative}')
