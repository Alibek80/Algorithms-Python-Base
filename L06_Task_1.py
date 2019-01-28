# Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы
# или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

# Python 3.7.0 on MacOS 10.14.2 64-bit
import sys
import random
import math


def show_size(x, level=0):
    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)


# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

def my_count(array1, array2):
    cnt = 0

    for i in array1:
        for j in array2:
            if i % j == 0:
                array1[i - 2] = 0

    for k in range(len(array1)):
        if array1[k] == 0:
            cnt += 1

    return [cnt, array1, array2, i, j, k]


array1 = list(range(2, 100))
array2 = list(range(2, 10))


# print(show_size(my_count(array1, array2)))

# type = <class 'list'>, size = 112, object = [77, [0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0, 19, 0, 0, 0, 23, 0, 0, 0, 0, 0, 29, 0, 31, 0, 0, 0, 0, 0, 37, 0, 0, 0, 41, 0, 43, 0, 0, 0, 47, 0, 0, 0, 0, 0, 53, 0, 0, 0, 0, 0, 59, 0, 61, 0, 0, 0, 0, 0, 67, 0, 0, 0, 71, 0, 73, 0, 0, 0, 0, 0, 79, 0, 0, 0, 83, 0, 0, 0, 0, 0, 89, 0, 0, 0, 0, 0, 0, 0, 97, 0, 0], [2, 3, 4, 5, 6, 7, 8, 9], 99, 9, 97]
# 	 type = <class 'int'>, size = 28, object = 77
# 	 type = <class 'list'>, size = 992, object = [0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0, 19, 0, 0, 0, 23, 0, 0, 0, 0, 0, 29, 0, 31, 0, 0, 0, 0, 0, 37, 0, 0, 0, 41, 0, 43, 0, 0, 0, 47, 0, 0, 0, 0, 0, 53, 0, 0, 0, 0, 0, 59, 0, 61, 0, 0, 0, 0, 0, 67, 0, 0, 0, 71, 0, 73, 0, 0, 0, 0, 0, 79, 0, 0, 0, 83, 0, 0, 0, 0, 0, 89, 0, 0, 0, 0, 0, 0, 0, 97, 0, 0]
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 11
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 13
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 17
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 19
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 23
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 29
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 31
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 37
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 41
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 43
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 47
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 53
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 59
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 61
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 67
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 71
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 73
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 79
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 83
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 89
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 97
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 	 type = <class 'list'>, size = 160, object = [2, 3, 4, 5, 6, 7, 8, 9]
# 		 type = <class 'int'>, size = 28, object = 2
# 		 type = <class 'int'>, size = 28, object = 3
# 		 type = <class 'int'>, size = 28, object = 4
# 		 type = <class 'int'>, size = 28, object = 5
# 		 type = <class 'int'>, size = 28, object = 6
# 		 type = <class 'int'>, size = 28, object = 7
# 		 type = <class 'int'>, size = 28, object = 8
# 		 type = <class 'int'>, size = 28, object = 9
# 	 type = <class 'int'>, size = 28, object = 99
# 	 type = <class 'int'>, size = 28, object = 9
# 	 type = <class 'int'>, size = 28, object = 97
# None

# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.


def even_array(array):
    array_new = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            array_new.append(i)
    return [array_new, array, i]


# print(show_size(even_array([random.randint(0, 100) for _ in range(10)])))
#  type = <class 'list'>, size = 88, object = [[0, 2, 3, 4, 6, 8, 9], [40, 95, 68, 36, 50, 97, 70, 3, 54, 46], 9]
# 	 type = <class 'list'>, size = 128, object = [0, 2, 3, 4, 6, 8, 9]
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 2
# 		 type = <class 'int'>, size = 28, object = 3
# 		 type = <class 'int'>, size = 28, object = 4
# 		 type = <class 'int'>, size = 28, object = 6
# 		 type = <class 'int'>, size = 28, object = 8
# 		 type = <class 'int'>, size = 28, object = 9
# 	 type = <class 'list'>, size = 192, object = [40, 95, 68, 36, 50, 97, 70, 3, 54, 46]
# 		 type = <class 'int'>, size = 28, object = 40
# 		 type = <class 'int'>, size = 28, object = 95
# 		 type = <class 'int'>, size = 28, object = 68
# 		 type = <class 'int'>, size = 28, object = 36
# 		 type = <class 'int'>, size = 28, object = 50
# 		 type = <class 'int'>, size = 28, object = 97
# 		 type = <class 'int'>, size = 28, object = 70
# 		 type = <class 'int'>, size = 28, object = 3
# 		 type = <class 'int'>, size = 28, object = 54
# 		 type = <class 'int'>, size = 28, object = 46
# 	 type = <class 'int'>, size = 28, object = 9
# None

# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.


def max_neg_value(array):
    max_neg_val = -math.inf
    max_neg_idx = 0

    for i in range(len(array)):
        if array[i] > max_neg_val and array[i] < 0:
            max_neg_val = array[i]
            max_neg_idx = i

    return [max_neg_val, max_neg_idx, array, i]

# print(show_size(max_neg_value([random.randint(-100, 100) for _ in range(10)])))
#
# type = <class 'list'>, size = 96, object = [-56, 2, [-60, -99, -56, -56, -83, 12, 36, 10, 5, 53], 9]
# 	 type = <class 'int'>, size = 28, object = -56
# 	 type = <class 'int'>, size = 28, object = 2
# 	 type = <class 'list'>, size = 192, object = [-60, -99, -56, -56, -83, 12, 36, 10, 5, 53]
# 		 type = <class 'int'>, size = 28, object = -60
# 		 type = <class 'int'>, size = 28, object = -99
# 		 type = <class 'int'>, size = 28, object = -56
# 		 type = <class 'int'>, size = 28, object = -56
# 		 type = <class 'int'>, size = 28, object = -83
# 		 type = <class 'int'>, size = 28, object = 12
# 		 type = <class 'int'>, size = 28, object = 36
# 		 type = <class 'int'>, size = 28, object = 10
# 		 type = <class 'int'>, size = 28, object = 5
# 		 type = <class 'int'>, size = 28, object = 53
# 	 type = <class 'int'>, size = 28, object = 9
# None