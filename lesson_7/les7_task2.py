# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


array = [random.choice([i for i in range(0, 50)]) for j in range(13)]
print(array)


# Функция слияния двух половин
def merger(left, right):
    res_lst = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res_lst.append(left[i])
            i += 1
        else:
            res_lst.append(right[j])
            j += 1

    # Добавляем остатки после окончания работы цикла слияния
    res_lst += left[i:]
    res_lst += right[j:]

    return res_lst


def merge_sort(array):
    # Базовый случай
    if len(array) == 1:
        return array

    # Дробление на половинки
    destruct = len(array) // 2
    return merger(merge_sort(array[:destruct]), merge_sort(array[destruct:]))


print(merge_sort(array))
