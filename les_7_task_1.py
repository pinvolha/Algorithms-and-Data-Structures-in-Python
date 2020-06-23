# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
import random


def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] < A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a


size = 20
array = [random.randint(-100, 100) for i in range(size)]
print(array)
bubble_sort(array)
print(array)
