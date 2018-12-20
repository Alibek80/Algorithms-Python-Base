# Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = int(input("Введите натуральное число: "))

sum1 = 0

for i in range(n+1):
    sum1 = sum1 + i

sum2 = n * (n + 1) / 2

if sum1 == sum2:
    print(f'Равенство верно для {n}')
else:
    print(f'Равенство не верно для {n}')