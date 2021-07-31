'''
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
'''
"""
Выбрана задача номер 4 урока 3: Определить, какое число в массиве встречается чаще всего.
"""
import random, collections, timeit, cProfile

#старая функция
a = [random.randint(1, 50) for i in range(30)]

def old(z):
    b = dict(collections.Counter(z))
    c = {x: y for x, y in filter(lambda x: b[x[0]] == max(b.values()), b.items())}
    return c
print(f'Случайный массив: {a}')
print(f'Чаще всего встречается: {old(a)}')

#новая функция
def new(z):
    numbers = dict()
    for item in z:
        if item not in numbers:
            numbers[item] = 1
        else:
            numbers[item] += 1
    max_count = 0
    num_max_count = []
    for num in numbers:
        if numbers[num] > max_count:
            max_count = numbers[num]
            num_max_count = [num]
        elif numbers[num] == max_count:
            num_max_count.append(num)
    return num_max_count, max_count

d, e = new(a)
print(f'Массив: {a}')
print(f'Число {d}, встречается {e} раза')

print(timeit.timeit(f'old({a})',globals=globals(), number=500))
print(timeit.timeit(f'new({a})',globals=globals(), number=500))
print(cProfile.run('old(a)'))
print(cProfile.run('new(a)'))

# 0.011323666999999996 - старая функция
# 0.0027693330000000058 - новая функция

# 87 function calls in 0.000 seconds - старая функция
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 __init__.py:540(__init__)
#         1    0.000    0.000    0.000    0.000 __init__.py:608(update)
#         1    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
#         1    0.000    0.000    0.000    0.000 homework4_1.py:13(old)
#         1    0.000    0.000    0.000    0.000 homework4_1.py:15(<dictcomp>)
#        25    0.000    0.000    0.000    0.000 homework4_1.py:15(<lambda>)
#         1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
#         1    0.000    0.000    0.000    0.000 {built-in method _collections._count_elements}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#        25    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
#        25    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
#

#          10 function calls in 0.000 seconds - новая функция
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 homework4_1.py:21(new)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         6    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#ВЫВОД
# Как мы видим, старая функция существенно отличается от новой и работает гораздо медленнее и не эффективно.