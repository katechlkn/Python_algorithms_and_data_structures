"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию:
Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
"""

import cProfile, timeit

def my_func(n):
    lst_prime = [2]
    number = 3
    while len(lst_prime) < n:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]

def func_eratosthenes(n):
    count = 1
    start = 3
    end = 4 * n
    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]
    if n == 1:
        return 2
    while count < n:
        for i in range(len(sieve)):
            if sieve[i] != 0:
                count += 1
                if count == n:
                    return sieve[i]
                j = i + sieve[i]
                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]
        prime.extend([i for i in sieve if i != 0])
        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]
        for i in range(len(sieve)):
            for num in prime:
                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break

a = int(input('Введите номер по счету простого числа: '))
print(f'Алгоритм 1 без использования алгоритма «Решето Эратосфена»: {my_func(a)} - {a} по счёту простое число')
print(f'Алгоритм 2 с использованием алгоритма «Решето Эратосфена»: {func_eratosthenes(a)} - {a} по счёту простое число')
print(cProfile.run('my_func(a)'))
print(cProfile.run('func_eratosthenes(a)'))
print(timeit.timeit(f'my_func({a})',globals=globals(), number=10))
print(timeit.timeit(f'func_eratosthenes({a})',globals=globals(), number=10))

# cProfile.run('my_func(10)')
# 68 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 homework4_2.py:11(my_func)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        28    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        27    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# print(cProfile.run('func_eratosthenes(10)'))
#          27 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 homework4_2.py:25(func_eratosthenes)
#         1    0.000    0.000    0.000    0.000 homework4_2.py:29(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        22    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('my_func(100)')
#          1182 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 homework4_2.py:11(my_func)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       540    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       539    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# print(cProfile.run('func_eratosthenes(100)'))
#          353 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 homework4_2.py:25(func_eratosthenes)
#         1    0.000    0.000    0.000    0.000 homework4_2.py:29(<listcomp>)
#         1    0.000    0.000    0.000    0.000 homework4_2.py:43(<listcomp>)
#         1    0.000    0.000    0.000    0.000 homework4_2.py:45(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       345    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


# cProfile.run('my_func(1000)')
#          16838 function calls in 0.037 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.037    0.037 <string>:1(<module>)
#         1    0.033    0.033    0.037    0.037 homework4_2.py:11(my_func)
#         1    0.000    0.000    0.037    0.037 {built-in method builtins.exec}
#      7918    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      7917    0.003    0.000    0.003    0.000 {method 'copy' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# print(cProfile.run('func_eratosthenes(1000)'))
#          4289 function calls in 0.022 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.022    0.022 <string>:1(<module>)
#         1    0.021    0.021    0.022    0.022 homework4_2.py:25(func_eratosthenes)
#         1    0.000    0.000    0.000    0.000 homework4_2.py:30(<listcomp>)
#         2    0.000    0.000    0.000    0.000 homework4_2.py:52(<listcomp>)
#         2    0.000    0.000    0.000    0.000 homework4_2.py:55(<listcomp>)
#         1    0.000    0.000    0.022    0.022 {built-in method builtins.exec}
#      4278    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
# Время выполнения нарастает. Рекурсий нет.


# print(timeit.timeit(f'my_func({a})',globals=globals(), number=10)) - 0.00016770900000029343
# print(timeit.timeit(f'func_eratosthenes({a})',globals=globals(), number=10)) - 0.00011270800000007242
# (0.00011270800000007242 * 100) /  0.00016770900000029343 = 100 - 67 = 33
# print(timeit.timeit(f'my_func({a})',globals=globals(), number=100)) - 0.05721987499999992
# print(timeit.timeit(f'func_eratosthenes({a})',globals=globals(), number=100)) - 0.02413962500000011
# (0.02413962500000011 * 100) / 0.05721987499999992 = 100 - 42 = 58
# print(timeit.timeit(f'my_func({a})',globals=globals(), number=1000)) - 34.868562917
# print(timeit.timeit(f'func_eratosthenes({a})',globals=globals(), number=1000)) - 20.534817832999998
# (20.534817832999998 * 100) / 34.868562917 = 100 - 59 = 41

# ВЫВОД:
# Сложность алгоритмов существенно отличаются: поиск номера с решетом Эратосфена выполняется быстрее и использует меньшее количество
# вызов функций и время работы на порядок ниже, почти в 2 раза, например, для поиска 1000 элемента используется 20,5 сек, когда
# алгоритм без решета использует 34,9 секунды.

