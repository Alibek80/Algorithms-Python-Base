# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
import cProfile


def generate_array(size, min_item, max_item):
    return [random.randint(min_item, max_item) for _ in range(size)]


def swap_min_max_1(size):
    array = generate_array(size, 0, 100)
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
    return array


def swap_min_max_2(size):
    array = generate_array(size, 0, 100)
    min_num = min(array)
    max_num = max(array)
    idx_min = array.index(min_num)
    idx_max = array.index(max_num)
    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    return array


# bash-3.2$ python -m timeit -n 10000 -s "import L04_Task_1" "L04_Task_1.swap_min_max_1(100)"

# 10000 loops, best of 5: 13.7 usec per loop - 10
# 10000 loops, best of 5: 26.1 usec per loop - 20
# 10000 loops, best of 5: 65.2 usec per loop - 50
# 10000 loops, best of 5: 128 usec per loop - 100
# 10000 loops, best of 5: 1.45 msec per loop - 1000


# bash-3.2$ python -m timeit -n 10000 -s "import L04_Task_1" "L04_Task_1.swap_min_max_2(10)"

# 10000 loops, best of 5: 13.5 usec per loop - 10
# 10000 loops, best of 5: 26 usec per loop - 20
# 10000 loops, best of 5: 62.1 usec per loop - 50
# 10000 loops, best of 5: 125 usec per loop - 100
# 10000 loops, best of 5: 1.45 msec per loop - 1000

# cProfile.run('swap_min_max_1(100)')
# 10
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:10(generate_array)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:11(<listcomp>)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:14(swap_min_max_1)
#        10    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:218(randint)
#        10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# 50
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:10(generate_array)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:11(<listcomp>)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:14(swap_min_max_1)
#        50    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        50    0.000    0.000    0.000    0.000 random.py:218(randint)
#        50    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        50    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        71    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# 100
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:10(generate_array)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:11(<listcomp>)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:14(swap_min_max_1)
#       100    0.000    0.000    0.000    0.000 random.py:174(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:218(randint)
#       100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       129    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('swap_min_max_2(100)')
# 10
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:10(generate_array)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:11(<listcomp>)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:35(swap_min_max_2)
#        10    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:218(randint)
#        10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        10    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# 50
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:10(generate_array)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:11(<listcomp>)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:35(swap_min_max_2)
#        50    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        50    0.000    0.000    0.000    0.000 random.py:218(randint)
#        50    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#        50    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        68    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# 100
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:10(generate_array)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:11(<listcomp>)
#         1    0.000    0.000    0.000    0.000 L04_Task_1.py:35(swap_min_max_2)
#       100    0.000    0.000    0.000    0.000 random.py:174(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:218(randint)
#       100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       125    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# Все алгоритмы имеют линейную зависимость от размера выборки
# - скорость и сложность растут линейно
