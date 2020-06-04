# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random
import timeit

# Для проведения замеров использовался массив из 1000 элементов
# array = [random.choice([i for i in range(-100, 100)]) for j in range(1000)]

array = [random.choice([i for i in range(-100, 100)]) for j in range(10)]
print(array)


# Пример из урока для тестов
def bubble_sort_1(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


# print(timeit.timeit('bubble_sort_1(array)', number=100, globals=globals())) # 9.7938432
print(bubble_sort_1(array))

# В функцию добавлен флаг для выхода из цикла в случае отсутствия операций перестановки. В отличии от варианта
# рассмотренного на уроке, в котором флаг уменьшал количество итераций цикла на 1 за каждый проход.

def bubble_sort_2(array):
    step = len(array) - 1
    for j in range(step):
        out = False
        for i in range(len(array) - j - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                out = True
        if not out:
            break
    return array


# print(timeit.timeit('bubble_sort_2(array)', number=100, globals=globals()))  # 0.23694920000000008
print(bubble_sort_2(array))
