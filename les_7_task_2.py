# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                a[k] = left[i]
                i = i + 1
            else:
                a[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            a[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            a[k] = right[j]
            j = j + 1
            k = k + 1


size = 20
array = [random.randint(0, 50) for i in range(size)]
print(array)
merge_sort(array)
print(array)
