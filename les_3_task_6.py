# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

size = int(input("Введите размер списка: "))
array = [randint(0, 50) for _ in range(size)]
print(f"{array}")
maxim = array[0]
minim = array[0]
index_max = 0
index_min = 0
s = 0

for i in range(1, size):
    if array[i] > maxim:
        maxim = array[i]
        index_max = i
    if array[i] < minim:
        minim = array[i]
        index_min = i

print(f'max {maxim}, min {minim}')

if index_min < index_max:
    for i in range(index_min + 1, index_max):
        s += array[i]
    print(f'Сумма элементов между max и min {s}')
elif index_min > index_max:
    for i in range(index_max + 1, index_min):
        s += array[i]
    print(f'Сумма элементов между max и min = {s}')
