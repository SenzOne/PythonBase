""" Задача 2:
Найдите сумму цифр трехзначного числа.
*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) """


def My_sum(num):
    first_num = num // 100
    second_num = num // 10 % 10
    third_num = num % 10
    res = first_num + second_num + third_num
    return f'{first_num} + {second_num} + {third_num} = {res}'


n = int(input("Введи число: "))
print(My_sum(n))
