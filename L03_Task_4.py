# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 20
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(SIZE)]

array2 = [0] * len(array)

for i in range(len(array)):
    for j in range(len(array)):
        if array[i] == array[j]:
            array2[i] = array2[i] + 1

max_cnt = 1
max_val = 0

for i in range(len(array2)):
    if array2[i] > max_cnt:
        max_cnt = array2[i]
        max_val = array[i]

print(max_val)
