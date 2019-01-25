# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив,
# элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

dec_lookup = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
              'C': 12, 'D': 13, 'E': 14, 'F': 15}

hex_lookup = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
              15: 'F'}


def dec_to_hex(decimal):
    result = deque()
    if decimal == 0:
        return '0'
    while decimal != 0:
        result.appendleft(str(hex_lookup[(decimal % 16)]))
        decimal = decimal // 16
    return result


def hex_to_dec(hexadecimal):
    n = len(hexadecimal)
    hexadecimal = hexadecimal.upper()
    hexadecimal = deque(hexadecimal)
    hexadecimal.reverse()
    result = 0
    if hexadecimal == '0':
        return 0

    for i in range(n):
        result = result + dec_lookup[hexadecimal[i]] * (16 ** i)

    return result


def hex_add(first, second):
    a = hex_to_dec(first)
    b = hex_to_dec(second)
    c = a + b
    result = dec_to_hex(c)
    return result


def hex_multi(first, second):
    a = hex_to_dec(first)
    b = hex_to_dec(second)
    c = a * b
    result = dec_to_hex(c)
    return result


a = 'A2'
b = 'C4F'
c = hex_add(a, b)
d = hex_multi(a, b)
print(c)
print(d)
