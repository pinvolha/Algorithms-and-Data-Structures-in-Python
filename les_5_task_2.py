# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict


def summary(number_sum, number_sum_2):
    result_list = []
    rev_number_1 = number_sum[::-1]
    rev_number_2 = number_sum_2[::-1]
    if len(rev_number_1) > len(rev_number_2):
        rev_number_2 = rev_number_2 + '0' * (len(rev_number_1) - len(rev_number_2))
    else:
        rev_number_1 = rev_number_1 + '0' * (len(rev_number_2) - len(rev_number_1))
    in_mind = 0
    for index, digit in enumerate(rev_number_1):
        result = my_converter[digit] + my_converter[rev_number_2[index]] + in_mind
        if result > 16:
            in_mind = result // 16
        else:
            in_mind = 0
        current_result = result - 16 * in_mind
        result = my_converter_reverse[str(current_result)]
        result_list.append(result)
    return list(reversed(result_list))


def multiplication(number_multi, number_multi_2):
    rev_number_1 = number_multi[::-1]
    rev_number_2 = number_multi_2[::-1]
    list_of_results = []
    for index, digit_2 in enumerate(rev_number_2):
        result_middle_list = []
        in_mind = 0
        for digit in rev_number_1:
            result_middle = my_converter[digit] * my_converter[digit_2] + in_mind
            if result_middle > 16:
                in_mind = result_middle // 16
            else:
                in_mind = 0
            current_result = result_middle - 16 * in_mind
            result = my_converter_reverse[str(current_result)]
            result_middle_list.append(result)
        if in_mind != 0:
            result_middle_list.append(str(in_mind))
        var_1 = list(reversed(result_middle_list))
        for j in range(index):
            var_1.append('0')
        list_of_results.append(var_1)
    for var_2 in range(0, len(list_of_results)-1, 1):
        number_first = ''.join(list_of_results[var_2])
        number_second = ''.join(list_of_results[var_2+1])
        calculation_result = summary(number_first, number_second)
        list_of_results[var_2+1] = calculation_result

    return list_of_results[len(list_of_results)-1]


my_converter = defaultdict(list,
                           {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                            'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
                           )

my_converter_reverse = defaultdict(list,
                                   {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7',
                                    '8': '8', '9': '9', '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E',
                                    '15': 'F'}
                                   )

number_1 = input('Введите первое число: ').upper()
number_2 = input('Введите второе число: ').upper()
print('Сумма чисел:', summary(number_1, number_2))
print('Произведение чисел:', multiplication(number_1, number_2))
