"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import defaultdict, deque

def func_dex(x):
    dex = 0
    number = deque(x)
    number.reverse()
    for i in range(len(number)):
        dex += dict_hexadecimal[number[i]] * 16 ** i
    return dex

def func_hex(x):
    number = deque()
    while x > 0:
        y = x % 16
        for i in dict_hexadecimal:
            if dict_hexadecimal[i] == y:
                number.append(i)
        x //= 16
    number.reverse()
    return list(number)

hexadecimal = '0123456789ABCDEF'
dict_hexadecimal = defaultdict(int)
counter = 0
for key in hexadecimal:
    dict_hexadecimal[key] += counter
    counter += 1

number_1 = func_dex(input('Введите первое число в шестнадцатиричном формате:\n ').upper())
number_2 = func_dex(input('Введите второе число в шестнадцатиричном формате:\n ').upper())

print(f'Сумма чисел: {func_hex(number_1 + number_2)}')
print(f'Произведение чисел: {func_hex(number_1 * number_2)}')