# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках

import random

M = 10
SIZE = 2 * M + 1
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(SIZE)]
array2 = array[:]

print(array)
print("*" * 50)


def gnome_sort(array):
    i = 1
    while i < len(array):
        if i == 0 or array[i - 1] <= array[i]:
            i += 1
        else:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
        print(array)
    return array


gnome_sort(array)
mediana = array[(len(array) // 2)]
print("Медина массива: ", mediana)
