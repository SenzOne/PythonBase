""" Задача 28:
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*

2 2
    4
"""


def rec_sum(a, b):
    if b == 1:
        return a + 1
    if b != 1:
        return a + rec_sum(1, b - 1)


A = int(input("Введи А: "))
B = int(input("Введи B: "))
print(rec_sum(A, B))