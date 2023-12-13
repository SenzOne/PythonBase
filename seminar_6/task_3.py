"""Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Вводится список чисел. Все числа списка находятся на разных строках."""
import random

my_list = [random.randint(1, 3) for x in range(5)]

print(my_list)


def Get_num(list1):
    uniq_dict = {}
    for i in list1:
        uniq_dict[i] = uniq_dict.get(i, 0) + 1
    return uniq_dict


def Get_couple(dict_n: dict):
    res_dict = {}
    for k, v in dict_n.items():
        if v % 2 == 0:
            res_dict[dict_n[k]] = v // 2
    return res_dict




print(Get_num(my_list))
print((Get_couple(Get_num(my_list))))
