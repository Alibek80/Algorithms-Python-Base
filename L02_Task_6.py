# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше
# или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

a = random.randint(0, 100)

for i in range(10):
    b = int(input("Введите целое число от 0 до 100: "))
    if b > a:
        print("Ваше число больше загаданного")
    elif b < a:
        print("Ваше число меньше загаданного")
    else:
        print(f"Вы угадали, загаданное число: {a}")
        break
    if i == 9:
        print(f"Вы не смогли угадать загаданное число, оно равно {a}")
