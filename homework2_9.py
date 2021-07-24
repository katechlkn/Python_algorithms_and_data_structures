"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

a = [i for i in input('Введите числа через пробел: ').split()]

def sum_numbers(number):
    sum = 0
    for el in number:
        sum += int(el)
    return sum

max_number = 0
max_sum = 0

for el in a:
    if sum_numbers(el) > max_sum:
        max_number = el
        max_sum = sum_numbers(el)

print(f'У числа {max_number} была наибольшая сумма цифр - {max_sum}')