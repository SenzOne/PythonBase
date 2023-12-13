"""Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списске A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
    1 2 3 4 5
    3
    -> 1 """
import random
count = int(input("Сколько чисел будет в списке?: "))
num_list = [random.randint(0, 5) for _ in range(count)]
print(*num_list, sep="  ")

res_dict = dict()
for i in num_list:
    if i in res_dict.keys():
        res_dict[i] += 1
    else:
        res_dict[i] = 1
n = int(input("Найти кол-во чисел: "))

print(f'чисел {n} в списке - {res_dict[n]}') if n in res_dict else print('Такого числа нет')
