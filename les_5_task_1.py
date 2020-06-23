# Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
# наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

Enterprise = namedtuple('Enterprise', ['q1', 'q2', 'q3', 'q4'])

n = int(input("Количество предприятий: "))
base_enterprise = {}

for i in range(n):
    name = input(str(i+1) + '-е предприятие: ')
    profit_q1 = int(input('Прибыль за 1-й квартал: '))
    profit_q2 = int(input('Прибыль за 2-й квартал: '))
    profit_q3 = int(input('Прибыль за 3-й квартал: '))
    profit_q4 = int(input('Прибыль за 4-й квартал: '))
    base_enterprise[name] = Enterprise(
        q1=profit_q1,
        q2=profit_q2,
        q3=profit_q3,
        q4=profit_q4
    )

total_profit = ()

for name, profit in base_enterprise.items():
    print(f'Предприятие {name}: прибыль за год - {sum(profit)}')
    total_profit += profit

avg_profit_total = sum(total_profit) / len(base_enterprise)
print(f'Средняя прибыль за год для всех предприятий {avg_profit_total}')

print('Предприятия, у которых прибыль выше среднего:')
for name, profit in base_enterprise.items():
    if sum(profit) > avg_profit_total:
        print(f'предприятие {name} - прибыль {sum(profit)}')

print('Предприятия, у которых прибыль ниже среднего:')
for name, profit in base_enterprise.items():
    if sum(profit) < avg_profit_total:
        print(f'предприятие {name} - прибыль {sum(profit)}')
