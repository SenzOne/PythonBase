"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*

5
    1 2 3 4 5
    6
    -> 5"""

import random


def Get_num(num_list):
    print(*num_list, sep="  ")
    res_dict = dict()
    for i in num_list:
        if i in res_dict.keys():
            res_dict[i] += 1
        else:
            res_dict[i] = 1
    return res_dict


def Get_adjacent_number(res_dict, number):
    key_to_list = list(res_dict.keys())
    min_key = abs(key_to_list[0] - number)
    found_key = 0
    for i in key_to_list:
        if abs(i - number) <= min_key:
            min_key = abs(i - number)
            found_key = i
    print(f'Числа {number} в списке нет, ближайшее к числу {number} - число {found_key} '
          f'встречается {res_dict[found_key]} раз(а)')


def Main():
    list_n = [random.randint(0, 20) for _ in range(10)]
    res = Get_num(list_n)
    n = int(input("Найти кол-во чисел: "))
    print(f'чисел {n} в списке - {res[n]}') if n in res else Get_adjacent_number(res, n)


Main()
