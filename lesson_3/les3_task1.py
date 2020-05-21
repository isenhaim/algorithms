# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

initial_list = [i for i in range(2, 100)]
num_list = [i for i in range(2, 10)]

for j in num_list:
    result_list = []
    for i in initial_list:
        if i % j == 0:
            result_list.append(i)

    print(f'Цифре {j} кратны: {len(result_list)} чисел')
