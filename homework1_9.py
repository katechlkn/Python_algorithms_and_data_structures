"""
9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

n = input('Введите три разных числа через запятую: ')
str = n.split(',')
print(sorted(str)[len(str) // 2])