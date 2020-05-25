# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.


# Задача ->
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random
import timeit
import cProfile

SIZE_1 = 10_000
SIZE_2 = 100_000
SIZE_3 = 1_000_000

MIN_ITEM = 0
MAX_ITEM = 100_000

array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_1)]
array_2 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_2)]
array_3 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_3)]

result_list = []

# Вариант решения при помощи тернарного оператора
def func_1(array):
    for i in range(len(array)):
        result_list.append(i) if array[i] % 2 == 0 else None
    return result_list


print(timeit.timeit('func_1(array_1)', number=100, globals=globals())) # 10_000 объектов 0.1623496000000002
print(timeit.timeit('func_1(array_2)', number=100, globals=globals())) # 100_000 объектов 1.7163161999999996
print(timeit.timeit('func_1(array_3)', number=100, globals=globals())) # 1_000_000 объектов 17.952790200000003

cProfile.run('func_1(array_1)') # 5049    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('func_1(array_2)') # 49768    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
cProfile.run('func_1(array_3)') # 501124    0.042    0.000    0.042    0.000 {method 'append' of 'list' objects}


# Вариант решения при помощи поиска по условию
def func_2(array):
    for i in range(len(array)):
        if array[i] % 2 == 0:
            result_list.append(i)
    return result_list


print(timeit.timeit('func_2(array_1)', number=100, globals=globals())) # 10_000 объектов 0.15803989999999857
print(timeit.timeit('func_2(array_2)', number=100, globals=globals())) # 100_000 объектов 2.102958700000002
print(timeit.timeit('func_2(array_3)', number=100, globals=globals())) # 1_000_000 объектов 21.295609399999996

cProfile.run('func_2(array_1)') # 5049    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
cProfile.run('func_2(array_2)') # 49768    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
cProfile.run('func_2(array_3)') # 501124    0.055    0.000    0.055    0.000 {method 'append' of 'list' objects}


# Вариант решения с использованием генератора
def func_3(array):
    result_list = [i for i in array if i % 2 == 0]
    return result_list


print(timeit.timeit('func_3(array_1)', number=100, globals=globals())) # 10_000 объектов 0.1321802999999946
print(timeit.timeit('func_3(array_2)', number=100, globals=globals())) # 100_000 объектов 1.388914100000001
print(timeit.timeit('func_3(array_3)', number=100, globals=globals())) # 1_000_000 объектов 9.486535699999997

cProfile.run('func_3(array_1)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 les4_task1.py:65(func_3)
#         1    0.001    0.001    0.001    0.001 les4_task1.py:66(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('func_3(array_2)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#         1    0.000    0.000    0.007    0.007 les4_task1.py:65(func_3)
#         1    0.007    0.007    0.007    0.007 les4_task1.py:66(<listcomp>)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('func_3(array_3)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.006    0.006    0.090    0.090 <string>:1(<module>)
#         1    0.000    0.000    0.084    0.084 les4_task1.py:65(func_3)
#         1    0.084    0.084    0.084    0.084 les4_task1.py:66(<listcomp>)
#         1    0.000    0.000    0.090    0.090 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# P.S Выбор пал именно на эту задачу т.к во время первого решения было два варианта решения описанные в func_1 и func_2
# Ранее использовал для проверки скорости модуль time и написание обрамлений для тестируемых функций
# занимало значительное время, timeit и cProfile стали открытием.

# По результатам анализа можно сделать вывод что все три варианты обладают сложностью O(n).
# Два первых практически идентичны как по времени так и по количеству вызова метода append
# Третий вариант показал наилучшие результаты по быстродействию, метод append вовсе не вызывается,
# что как видно экономит наше время.
