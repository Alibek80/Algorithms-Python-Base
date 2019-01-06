# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

cnt = 0
array1 = list(range(2, 100))
array2 = list(range(2, 10))

for i in array1:
    for j in array2:
        if i % j == 0:
            array1[i - 2] = 0

for k in range(len(array1)):
    if array1[k] == 0:
        cnt += 1

print(cnt)
