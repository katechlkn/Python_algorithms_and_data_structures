"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
import random
a = [random.randint(1, 30) for i in range(15)]
print(f'Массив целый чисед: {a}')
a = sorted(a, reverse=False)
print(f'Два наименьших элемента массива: {a[0]}, {a[1]}')
