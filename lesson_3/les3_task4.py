# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

count = 0
num = None


for i in array:
    result_list = []
    for j in array:
        if i == j:
            result_list.append(j)

    if count < len(result_list):
        count = len(result_list)
        num = i
    array.remove(i)

print(f'В массиве чаще всего встречается число {num}, {count} раз(а)')
