"""
7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков.
Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

ps for me. Треугольник существует только тогда, когда сумма длин любых его двух сторон больше третьей стороны.
"""

n = input('Введите длины трех отрезков через запятую: ')
str = n.split(',')

if int(str[0]) + int(str[1]) <= int(str[2]) or int(str[1]) + int(str[2]) <= int(str[0]) or int(str[0]) + int(str[2]) <= int(str[1]):
    print('Такого треугольника не существует.')
elif str[0] != str[1] and str[1] != str[2] and str[0] != str[2]:
    print('Треугольник разносторонний')
elif str[0] == str[1] == str[2]:
    print('Треугольник равносторонний')
else:
    print('Треугольник равнобедренный')