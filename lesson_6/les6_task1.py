# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
#   ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
#   ● написать 3 варианта кода (один у вас уже есть);
#   ● проанализировать 3 варианта и выбрать оптимальный;
#   ● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл
#   с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
#   ● написать общий вывод: какой из трёх вариантов лучше и почему.
#
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
# а проявили творчество, фантазию и создали универсальный код для замера памяти.


import random
import sys
from collections import Counter

from memory_profiler import profile


# Функция подсчета общей занимаемой памяти рядом переменных
def total_memory(*variable):
    size = 0
    for i in variable:
        size += sys.getsizeof(i)
    return size


# Для анализа выбрана задача ->

# Определить, какое число в массиве встречается чаще всего.
SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


# Первое уже имеющееся решение из ПЗ №3
@profile
def func_1(array):
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

    print(f'В массиве чаще всего встречается число {num}, {count} раз(а)'
          f'\nОбъем занимаемой памяти {total_memory(count, num, result_list, i, j)} байт(а)')


# Решение с использованием Counter
@profile
def func_2(array):
    result = Counter(array).most_common(1)
    print(f'В массиве чаще всего встречается число {result[0][0]}, {result[0][1]} раз(а). '
          f'\nОбъем занимаемой памяти {total_memory(result)} байт(а)')


# Решение без дополнительного списка
@profile
def func_3(array):
    result = array.count(array[0])
    max_num = array[0]
    for i in array:
        if array.count(i) > result:
            result = array.count(i)
            max_num = i

    print(f'В массиве чаще всего встречается число {max_num}, {result} раз(а). '
          f'\nОбъем занимаемой памяти {total_memory(result, max_num, i)} байт(а)')


func_1(array)

# В массиве чаще всего встречается число 6, 111 раз(а)
# Объем занимаемой памяти 1016 байт(а)


# Filename: C:/Users/Евгений/Desktop/algorithms/lesson_6/les6_task1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     42     52.6 MiB     52.6 MiB   @profile
#     43                             def func_1(array):
#     44     52.6 MiB      0.0 MiB       count = 0
#     45     52.6 MiB      0.0 MiB       num = None
#     46
#     47     52.6 MiB      0.0 MiB       for i in array:
#     48     52.6 MiB      0.0 MiB           result_list = []
#     49     52.6 MiB      0.0 MiB           for j in array:
#     50     52.6 MiB      0.0 MiB               if i == j:
#     51     52.6 MiB      0.0 MiB                   result_list.append(j)
#     52
#     53     52.6 MiB      0.0 MiB           if count < len(result_list):
#     54     52.6 MiB      0.0 MiB               count = len(result_list)
#     55     52.6 MiB      0.0 MiB               num = i
#     56
#     57     52.5 MiB      0.0 MiB       print(f'В массиве чаще всего встречается число {num}, {count} раз(а)'
#     58                                       f'\nОбъем памяти {total_memory(count, num, result_list, i, j)} байт(а)')

func_2(array)

# В массиве чаще всего встречается число 6, 111 раз(а).
# Объем занимаемой памяти 64 байт(а)


# Filename: C:/Users/Евгений/Desktop/algorithms/lesson_6/les6_task1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     64     52.5 MiB     52.5 MiB   @profile
#     65                             def func_2(array):
#     66     52.5 MiB      0.0 MiB       result = Counter(array).most_common(1)
#     67     52.5 MiB      0.0 MiB       print(f'чаще всего встречается число {result[0][0]}, {result[0][1]} раз(а). '
#     68                                       f'\nОбъем занимаемой памяти {total_memory(result)} байт(а)')


func_3(array)

# В массиве чаще всего встречается число 6, 111 раз(а).
# Объем занимаемой памяти 84 байт(а)


# Filename: C:/Users/Евгений/Desktop/algorithms/lesson_6/les6_task1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     72     52.5 MiB     52.5 MiB   @profile
#     73                             def func_3(array):
#     74     52.5 MiB      0.0 MiB       result = array.count(array[0])
#     75     52.5 MiB      0.0 MiB       max_num = array[0]
#     76     52.5 MiB      0.0 MiB       for i in array:
#     77     52.5 MiB      0.0 MiB           if array.count(i) > result:
#     78     52.5 MiB      0.0 MiB               result = array.count(i)
#     79     52.5 MiB      0.0 MiB               max_num = i
#     80
#     81     52.5 MiB      0.0 MiB       print(f'В массиве чаще всего встречается число {max_num}, {result} раз(а). '
#     82                                       f'\nОбъем занимаемой памяти {total_memory(result, max_num, i)} байт(а)')
#


# Характеристики системы и интерпритатора
# 'AMD64'
# Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32

# По результатам:
#
#   * func_1 - плохая реализация, занимает место под дополнительный список, имеет две переменные для  извлечения
#     значений списка.
#
#   * func_2 - наиболее оптимальный вариант меньше памяти, меньше циклов и кода. По скорости работы так же значительно
#     превосходит два других варианта. Тот случай когда суть задачи и коллекция (Counter) были созданы друг для друга.
#
#   * func_3 - не самый плохой вариант, нет доп. списка как в func_1, переменная для извлечения значений массива одна.
#
# В итоге func_2 c использованием Counter превосходит остальные по оптимальности для данной задачи.
