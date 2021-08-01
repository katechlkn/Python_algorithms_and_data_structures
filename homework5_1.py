"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections

while True:
    try:
        n = int(input('Введите количество предприятий для ввода данных: '))
    except ValueError:
        print('Вы ввели недопустимое значение, введите целое число.')
        continue
    break

companies = []

for i in range(n):
    title_company = input(f'Введите наименование {i+1} предприятия: ')
    profit1, profit2, profit3, profit4 = map(int, input('Квартальные прибыли через пробел: ').split(' '))
    company = {
        "Наименование предприятия": title_company,
        "Прибыль за 1 квартал": profit1,
        "Прибыль за 2 квартал": profit2,
        "Прибыль за 3 квартал": profit3,
        "Прибыль за 4 квартал": profit4,
        "Прибыль предприятия за год": profit1 + profit2 + profit3 + profit4
    }
    companies.append(company)

for company in companies:
    print(company)

profit_col = collections.Counter()
for company in companies:
    profit_comp = company.copy()
    del profit_comp['Наименование предприятия']
    profit_col += profit_comp

average_profit = profit_col['Прибыль предприятия за год'] / len(companies)

print('Суммарная прибыль компаний: ', profit_col)
print('Средняя годовая прибыль компаний: ', average_profit)
print('Прибыль выше среднего: ', [x['Наименование предприятия'] for x in companies if x['Прибыль предприятия за год'] >= average_profit])
print('Прибыль ниже среднего: ', [x['Наименование предприятия'] for x in companies if x['Прибыль предприятия за год'] < average_profit])


