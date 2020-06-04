# 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.

# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).
import random


n = 4
array = [random.choice([i for i in range(0, 100)]) for j in range(n * 2 + 1)]
print(array)


def search_median(array):
    for i in array:
        max_num = 0
        min_num = 0

        for j in array:
            if i <= j:
                max_num += 1
            elif i > j:
                min_num += 1

        if max_num - 1 == min_num:
            return i


print(f'Медиана массива {search_median(array)}')


def test(array, func):
    array = sorted(array)
    result = array[len(array) // 2]

    if result == func(array):
        return 'Ok'
    return 'You\'re weak'


print(f'Результат теста {test(array, search_median)}')
