# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

n = int(input("Введите номер буквы в алфавите: "))
alf = 'abcdefghijklmnopqrstuvwxyz'
letter = alf[n - 1]
print("Это буква", letter.upper())
