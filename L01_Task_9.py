# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input("Введите первое число: "))

b = int(input("Введите второе число: "))

c = int(input("Введите третье число: "))

if a > b:
    if b > c:
        print(b)
    else:
        if c > a:
            print(a)
        else:
            print(c)
else:
    if c > b:
        print(b)
    else:
        if a > c:
            print(a)
        else:
            print(c)
