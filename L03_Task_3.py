# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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

array[min_idx] = max_val
array[max_idx] = min_val

print(array)
