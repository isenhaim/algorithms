# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

company = namedtuple('company', 'name revenue')
cnt = int(input('Введите кол-во компаний для подсчета: '))
company_lst = []


for i in range(cnt):
    company_name = input(f'{i + 1} компания: ')
    revenue = []

    for i in range(4):
        revenue.append(int(input(f'Доход за {i + 1} квартал: ')))

    company_lst.append(company(company_name, revenue))

sum_rev = 0
for i in company_lst:
    sum_rev += sum(i.revenue)

average = sum_rev / len(company_lst)

print(f'Средний доход всех компаний {average}')

up = [i.name for i in company_lst if sum(i.revenue) > average]
down = [i.name for i in company_lst if sum(i.revenue) < average]

print(f'Доход выше среднего у компании: {", ".join(up)}')
print(f'Доход ниже среднего у компании: {", ".join(down)}')
