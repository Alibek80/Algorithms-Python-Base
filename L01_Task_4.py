# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
#
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

a1 = int(input("Введите нижнюю границу для целых чисел: "))
a2 = int(input("Введите верхнюю границу для целых чисел: "))

b1 = float(input("Введите нижнюю границу для вещественных чисел: "))
b2 = float(input("Введите верхнюю границу для вещественных чисел: "))

c1 = input("Введите нижнюю границу для символов: ")
c2 = input("Введите верхнюю границу для символов: ")

rnd1 = random.randint(a1, a2)
rnd2 = random.random() * (b2 - b1) + b1
rnd3 = chr(random.randint(ord(c1), ord(c2)))

print(rnd1)
print(rnd2)
print(rnd3)