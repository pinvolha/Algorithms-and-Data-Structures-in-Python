# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * задача считается решённой, если в коде использована функция вычисления хеша (hash(),
# sha1() или любая другая из модуля hashlib)
from hashlib import sha1


def count_subs(string):
    result = set()

    for i in range(1, len(string)):
        for j in range(len(string) - i):
            h = sha1(string[j:i+j])
            result.add(h)

    return len(result)


s = input('Введите строку: ').encode('utf-8')

print(f'В данной строке {count_subs(s)} различных подстрок')
