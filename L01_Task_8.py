# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

y = int(input("Введите год: "))

if y % 4 == 0 or y % 400:
    print("Указанный год является високосным")
else:
    print("Указанный год - не високосный")