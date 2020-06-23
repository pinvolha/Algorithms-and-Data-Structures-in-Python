# Проанализировать скорость и сложность алгоритмов.
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

import random


def even_search(size):
    array = [random.randint(0, 100) for _ in range(size)]
    even_array = []
    for i in range(size):  # используется перебор массива по индексу
        if array[i] % 2 == 0:
            even_array.append(i)


# py -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.even_search(100)"
# 1000 loops, best of 5: 348 usec per loop
# py -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.even_search(1000)"
# 1000 loops, best of 5: 3.6 msec per loop


def even_search2(size):
    array = [random.randint(0, 100) for _ in range(size)]
    even_array = []
    for item in array:    # используется перебор элементов массива с последующим нахождением индекса
        if item % 2 == 0:
            even_array.append(array.index(item))

# py -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.even_search2(100)"
# 1000 loops, best of 5: 416 usec per loop
# py -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.even_search2(1000)"
# 1000 loops, best of 5: 5.27 msec per loop


# вывод: перебирать индексы быстрее, чем перебирать элементы массива и потом искать индексы нужных