# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

size = int(input("Введите размер списка: "))
array = [randint(-100, 100) for _ in range(size)]
print(f"{array} Исходный массив")
maxim = array[0]
minim = array[0]
index_max = 0
index_min = 0

for i in range(1, size):
    if array[i] > maxim:
        maxim = array[i]
        index_max = i
    if array[i] < minim:
        minim = array[i]
        index_min = i

array[index_min], array[index_max] = array[index_max], array[index_min]
print(f"{array} Массив после замены max и min")
