# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

a = 0
sum_a = 0

while True:
    b = int(input("Введите натуральное число (при вводе 0 запрос на ввод дополнительных чисел прекратится): "))
    e = b
    sum_b = 0
    if b == 0:
        break
    c = len(str(b))
    for i in range(c):
        d = b % 10
        sum_b = sum_b + d
        b = b // 10
    if sum_b > sum_a:
        sum_a = sum_b
        a = e

print(f"Число с наибольшей суммой цифр составляет {a}, а сумма цифр - {sum_a}")
