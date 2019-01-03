# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(SIZE)]

print(array)

min_val = array[0]
min_idx = 0

max_val = array[0]
max_idx = 0

for i in range(len(array)):
    if array[i] < min_val:
        min_val = array[i]
        min_idx = i
    elif array[i] > max_val:
        max_val = array[i]
        max_idx = i

if min_idx < max_idx:
    array_sum = sum(array[min_idx + 1:max_idx])
elif min_idx > max_idx:
    array_sum = sum(array[max_idx + 1:min_idx])
else:
    array_sum = 0

print(array_sum)
