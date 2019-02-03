# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
min_item = 0
max_item = 50 - 10 ** -7
array = [random.uniform(min_item, max_item) for _ in range(SIZE)]

f_array = [round(elem, 2) for elem in array]
print(f_array)
print("*" * 50)


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        middle = int(len(array) / 2)
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


sort_array = merge_sort(array)
sort_array = [round(elem, 2) for elem in sort_array]
print(sort_array)
