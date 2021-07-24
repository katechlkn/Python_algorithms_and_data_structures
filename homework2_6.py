"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
"""
import random

a = random.randint(0, 100)
count = 1
while count <= 10:
    b = int(input('Введите целое число от 0 до 100: '))
    if a == b:
        print('Вы угадали!')
        break
    elif a < b:
        print(f'Загаданное число меньше, у вас осталось {10 - count} попыток')
    elif a > b:
        print(f'Загаданное число больше, у вас осталось {10 - count} попыток')
    count += 1
else:
    print(f'К сожалению, вы не угадали, загаданное число - {a}')