"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две
равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
то используйте метод сортировки, который не рассматривался на уроках
"""

import random

m = random.randint(1, 10)
n = 2 * m + 1
array = [random.randint(1, 10) for i in range(n)]

def partition(a, i, j):
    v = a[(i + j)//2]
    while i <= j:
        while a[i] < v:
            i += 1
        while a[j] > v:
            j -= 1
        if i <= j:
            a[i],a[j] = a[j],a[i]
            i += 1
            j -= 1
    return j

def mediana(a):
    k, left, right = len(a) // 2, 0, len(a) - 1
    while True:
        mid = partition(a, left, right)
        if mid == k:
            return a[mid]
        if k < mid:
            right = mid
        else:
            left = mid + 1

print(f'Исходный массив: {array}')
print(f'Медиана массива: {mediana(array)}')
