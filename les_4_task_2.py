# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
import cProfile


def eratosthenes_sieve(n):
    count = 1
    start = 3
    end = 4 * n

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2
    while count < n:
        for i in range(len(sieve)):
            if sieve[i] != 0:
                count += 1
                if count == n:
                    return sieve[i]
                j = i + sieve[i]
                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]
        prime.extend([i for i in sieve if i != 0])
        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(sieve)):
            for num in prime:
                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break

# py -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.eratosthenes_sieve(10)"
# "les_4_task_2.eratosthenes_sieve(10)"
# 100 loops, best of 5: 23 usec per loop
# "les_4_task_2.eratosthenes_sieve(100)"
# 100 loops, best of 5: 917 usec per loop
# "les_4_task_2.eratosthenes_sieve(1000)"
# 100 loops, best of 5: 81.3 msec per loop

# cProfile.run('eratosthenes_sieve(10)')
# 27 function calls in 0.000 seconds
# cProfile.run('eratosthenes_sieve(100)')
# 353 function calls in 0.014 seconds


def search_prime(n):
    count = 1
    number = 1
    prime = [2]
    if n == 1:
        return 2
    while count != n:
        number += 2
        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)
    return number

# py -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.search_prime(10)"
# "les_4_task_2.search_prime(10)"
# 100 loops, best of 5: 15.9 usec per loop
# "les_4_task_2.search_prime(100)"
# 100 loops, best of 5: 906 usec per loop
# "les_4_task_2.search_prime(1000)"
# 100 loops, best of 5: 79.4 msec per loop
# Скорость работы обоих алгоритмов на данных объемах данных практически одинакова.

# cProfile.run('search_prime(10)')
# 13 function calls in 0.000 seconds

# cProfile.run('search_prime(100)')
# 103 function calls in 0.001 seconds


# ВЫВОД: Сложность алгоритмов и время их работы приблизительно одинаковые.
