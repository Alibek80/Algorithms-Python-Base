# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random

SIZE = 10
min_item = -100
max_item = 99
array = [random.randint(min_item, max_item) for _ in range(SIZE)]
array2 = array[:]

print(array)
print("*" * 50)


def bubble_sort(array):
    n = 1
    c = 0
    while n < len(array):

        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                c += 1

        n += 1
        print(array, c)


def bubble_sort2(array):
    n = 1
    c = 0
    while n < len(array):

        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                c += 1

        n += 1
        print(array, c)


bubble_sort(array)
print("*" * 50)
bubble_sort2(array2)
