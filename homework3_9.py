"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random

a = []
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(random.randint(0, 99))

min_list = []
min_list.extend(a[0])

for el in a:
    print(('{:>4d} ' * len(el)).format(*el))
    i = 0
    for j in el:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print('_' * 27)
print(('{:4d} ' * len(min_list)).format(*min_list))

min_list.sort(reverse=True)
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {min_list[0]}')