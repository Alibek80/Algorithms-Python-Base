# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
min_item = -100
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(SIZE)]

print(array)

max_neg_val = min_item
max_neg_idx = 0

for i in range(len(array)):
    if array[i] > max_neg_val and array[i] < 0:
        max_neg_val = array[i]
        max_neg_idx = i

print(max_neg_val, max_neg_idx)
