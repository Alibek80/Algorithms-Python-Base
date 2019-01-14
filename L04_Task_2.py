# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»

import cProfile


def primes_not_sieve(n):
    lst = []
    i = 2
    while len(lst) < n:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
        i = i + 1
    return lst [n]


def primes_sieve(n):
    result = []
    m = n * n
    while len(result) < n:
        sieve = [i for i in range(m)]

        sieve[1] = 0
        for i in range(2, m):
            if sieve[i] != 0:
                j = i + i
                while j < m:
                    sieve[j] = 0
                    j += i

        result = [i for i in sieve if i != 0]
        m = m + 1
    return result[n]


# bash-3.2$ python -m timeit -n 10000 -s "import L04_Task_2" "L04_Task_2.primes_not_sieve(10)"
# 10000 loops, best of 5: 16.2 usec per loop - 10
# 10000 loops, best of 5: 54.5 usec per loop - 20
# 10000 loops, best of 5: 308 usec per loop - 50
# 10000 loops, best of 5: 1.42 msec per loop - 100

# bash-3.2$ python -m timeit -n 10000 -s "import L04_Task_2" "L04_Task_2.primes_sieve(10)"
# 10000 loops, best of 5: 21.6 usec per loop
# 10000 loops, best of 5: 99.1 usec per loop
# 10000 loops, best of 5: 772 usec per loop
# 10000 loops, best of 5: 3.45 msec per loop

# cProfile.run('primes_not_sieve(100)')
# 10
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 L04_Task_2.py:8(primes_not_sieve)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        29    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 50
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 L04_Task_2.py:8(primes_not_sieve)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       229    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        50    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 100
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.004    0.004    0.005    0.005 L04_Task_2.py:8(primes_not_sieve)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#       541    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('primes_sieve(100)')
# 10
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# #         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# #         1    0.000    0.000    0.000    0.000 L04_Task_2.py:21(primes_sieve)
# #         1    0.000    0.000    0.000    0.000 L04_Task_2.py:25(<listcomp>)
# #         1    0.000    0.000    0.000    0.000 L04_Task_2.py:35(<listcomp>)
# #         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# #         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# #         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 50
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 L04_Task_2.py:21(primes_sieve)
#         1    0.000    0.000    0.000    0.000 L04_Task_2.py:25(<listcomp>)
#         1    0.000    0.000    0.000    0.000 L04_Task_2.py:35(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 100
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.013    0.013 <string>:1(<module>)
#         1    0.010    0.010    0.013    0.013 L04_Task_2.py:21(primes_sieve)
#         1    0.001    0.001    0.001    0.001 L04_Task_2.py:25(<listcomp>)
#         1    0.001    0.001    0.001    0.001 L04_Task_2.py:35(<listcomp>)
#         1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Первый алогоритм имеет нелинейную зависимость сложности и скорости
# Второй алгоритм имеет нелинейную зависимость от скорости и линейную сложность
