# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
from sys import getsizeof


def show_size(x, level=0):
    result_size = getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                result_size += show_size(key, level + 1)
                result_size += show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                result_size += show_size(item, level + 1)
    return result_size


def local_var_size(local_var):
    local_variables_dict = locals().copy()
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show_size(local_variables_dict[var])
    print(f'Список всех переменных: {local_variables_dict}')
    return print(f'Общий размер используемых переменных в функции: {size_of_all_variables} байт')


# Функция поиска буквы по номеру из алфавита, представленного строкой
def find_letter1(n):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    local_variables_dict = locals().copy()
    local_var_size(local_variables_dict)
    if n <= 0 or n > len(abc):
        return 'error'
    else:
        return print("Это буква", abc[n - 1].upper())


# Функция поиска буквы по ее номеру в кодировке
def find_letter2(n):
    local_variables_dict = locals().copy()
    local_var_size(local_variables_dict)
    if (n + 96) < 97 or (n + 96) > 122:
        return 'error'
    else:
        return print("Это буква", chr(n + 96).upper())


# Функция поиска буквы по номеру из алфавита, представленного списком
def find_letter3(n):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    local_variables_dict = locals().copy()
    local_var_size(local_variables_dict)
    return print("Это буква", abc[n - 1].upper())


find_letter1(2)
print('*' * 20)
find_letter2(2)
print('*' * 20)
find_letter3(2)

# Меньше всего памяти занимает функция поиска буквы по ее номеру в кодировке.
# Больше всего - где алфавит представлен списком.

#  type=<class 'dict'>, size=128, obj={'n': 2, 'abc': 'abcdefghijklmnopqrstuvwxyz'}
# 	 type=<class 'str'>, size=26, obj=n
# 	 type=<class 'int'>, size=14, obj=2
# 	 type=<class 'str'>, size=28, obj=abc
# 	 type=<class 'str'>, size=51, obj=abcdefghijklmnopqrstuvwxyz
# Список всех переменных: {'local_var': {'n': 2, 'abc': 'abcdefghijklmnopqrstuvwxyz'}}
# Общий размер используемых переменных в функции: 247 байт
# Это буква B
# ********************
#  type=<class 'dict'>, size=128, obj={'n': 2}
# 	 type=<class 'str'>, size=26, obj=n
# 	 type=<class 'int'>, size=14, obj=2
# Список всех переменных: {'local_var': {'n': 2}}
# Общий размер используемых переменных в функции: 168 байт
# Это буква B
# ********************
#  type=<class 'dict'>, size=128, obj={'n': 2, 'abc': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']}
# 	 type=<class 'str'>, size=26, obj=n
# 	 type=<class 'int'>, size=14, obj=2
# 	 type=<class 'str'>, size=28, obj=abc
# 	 type=<class 'list'>, size=132, obj=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# 		 type=<class 'str'>, size=26, obj=a
# 		 type=<class 'str'>, size=26, obj=b
# 		 type=<class 'str'>, size=26, obj=c
# 		 type=<class 'str'>, size=26, obj=d
# 		 type=<class 'str'>, size=26, obj=e
# 		 type=<class 'str'>, size=26, obj=f
# 		 type=<class 'str'>, size=26, obj=g
# 		 type=<class 'str'>, size=26, obj=h
# 		 type=<class 'str'>, size=26, obj=i
# 		 type=<class 'str'>, size=26, obj=j
# 		 type=<class 'str'>, size=26, obj=k
# 		 type=<class 'str'>, size=26, obj=l
# 		 type=<class 'str'>, size=26, obj=m
# 		 type=<class 'str'>, size=26, obj=n
# 		 type=<class 'str'>, size=26, obj=o
# 		 type=<class 'str'>, size=26, obj=p
# 		 type=<class 'str'>, size=26, obj=q
# 		 type=<class 'str'>, size=26, obj=r
# 		 type=<class 'str'>, size=26, obj=s
# 		 type=<class 'str'>, size=26, obj=t
# 		 type=<class 'str'>, size=26, obj=u
# 		 type=<class 'str'>, size=26, obj=v
# 		 type=<class 'str'>, size=26, obj=w
# 		 type=<class 'str'>, size=26, obj=x
# 		 type=<class 'str'>, size=26, obj=y
# 		 type=<class 'str'>, size=26, obj=z
# Список всех переменных: {'local_var': {'n': 2, 'abc': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']}}
# Общий размер используемых переменных в функции: 1004 байт
# Это буква B