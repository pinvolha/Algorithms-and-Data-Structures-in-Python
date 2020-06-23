# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
import random


def shaker_sort(a):
    for i in range(len(a) - 1):
        for j in range(i, len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

        for j in range(len(a) - 2, i, -1):
            if a[j - 1] > a[j]:
                a[j], a[j - 1] = a[j - 1], a[j]


def mediana(A):
    shaker_sort(A)
    print(A)
    return A[len(A) // 2]


size = 10
array = [random.randint(0, 50) for i in range(2 * size + 1)]
print(array)
print(mediana(array))
