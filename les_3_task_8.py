# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

print("Enter values in matrix:")
matrix = [[int(input()) for _ in range(4)] for _ in range(4)]

for line in matrix:
    sum_line = 0

    for i in range(len(line)):
        sum_line += line[i]
        print(f'{line[i]:>5}', end='')

    print(f'   {sum_line}')
