"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random, collections

a = [random.randint(1, 50) for i in range(30)]
b = dict(collections.Counter(a))
c = {x: y for x, y in filter(lambda x: b[x[0]] == max(b.values()), b.items())}

print(f'Случайный массив: {a}')
print(f'Чаще всего встречается: {c}')
