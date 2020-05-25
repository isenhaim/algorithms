# 2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
# улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
import cProfile
import timeit

n = 100000

sieve = [i for i in range(n)]
sieve[1] = 0


def func_1(num):
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    return res[num]


print(timeit.timeit('func_1(10)', number=100, globals=globals()))  # 8.714362699999999
print(timeit.timeit('func_1(100)', number=100, globals=globals()))  # 8.9212782
print(timeit.timeit('func_1(1000)', number=100, globals=globals()))  # 9.6131308

cProfile.run('func_1(10)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.088    0.088 <string>:1(<module>)
#      1    0.084    0.084    0.088    0.088 les4_task2.py:19(func_1)
#      1    0.004    0.004    0.004    0.004 les4_task2.py:27(<listcomp>)
#      1    0.000    0.000    0.088    0.088 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('func_1(100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.041    0.041 <string>:1(<module>)
#      1    0.038    0.038    0.041    0.041 les4_task2.py:19(func_1)
#      1    0.004    0.004    0.004    0.004 les4_task2.py:27(<listcomp>)
#      1    0.000    0.000    0.042    0.042 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('func_1(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.069    0.069 <string>:1(<module>)
#      1    0.060    0.060    0.069    0.069 les4_task2.py:19(func_1)
#      1    0.009    0.009    0.009    0.009 les4_task2.py:27(<listcomp>)
#      1    0.000    0.000    0.069    0.069 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Функция проверки на простоту числа
def prime(num):
    start_num = 2
    while start_num * start_num <= num and num % start_num != 0:
        start_num += 1
    return start_num * start_num > num


# Функция получения n простого элемента
def func_2(num):
    i = 2
    result = []
    while len(result) <= num:
        result.append(i) if prime(i) else None
        i += 1
    return result[num]


print(timeit.timeit('func_2(10)', number=100, globals=globals()))  # 0.0030862999999999863
print(timeit.timeit('func_2(100)', number=100, globals=globals()))  # 0.12014049999999998
print(timeit.timeit('func_2(1000)', number=100, globals=globals()))  # 2.5847578

cProfile.run('func_2(10)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     30    0.000    0.000    0.000    0.000 les4_task2.py:61(prime)
#      1    0.000    0.000    0.000    0.000 les4_task2.py:69(func_2)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     31    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     11    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('func_2(100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#    546    0.001    0.000    0.001    0.000 les4_task2.py:61(prime)
#      1    0.000    0.000    0.001    0.001 les4_task2.py:69(func_2)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#    547    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    101    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('func_2(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.029    0.029 <string>:1(<module>)
#   7926    0.021    0.000    0.021    0.000 les4_task2.py:61(prime)
#      1    0.006    0.006    0.029    0.029 les4_task2.py:69(func_2)
#      1    0.000    0.000    0.029    0.029 {built-in method builtins.exec}
#   7927    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#   1001    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Просто оставлю это здесь, но лучше не запускать, наихудший вариант, оставлен как экперимент
# генераторы не всегда хороши
def func_3(num):
    result = [i for i in range(2, num * num) if prime(i)]
    return result[num]

# print(timeit.timeit('func_3(10)', number=100, globals=globals())) # 0.005620199999999964
# print(timeit.timeit('func_3(100)', number=100, globals=globals())) # 2.258666
# print(timeit.timeit('func_3(1000)', number=100, globals=globals())) #
#
# cProfile.run('func_3(10)')
# cProfile.run('func_3(100)')
# cProfile.run('func_3(1000)')


# P.S анализ вариантов показал что наиболее оптимальным является вариант c функцией func_2
