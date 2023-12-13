"""Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1,
но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите
все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k,
не превосходящее 105. Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k."""


# def Get_dev(n):
#     div_list_1 = []
#     for i in range(n, 1, -1):
#         if n % i == 0:
#             div_list_1.append(i)
#     return div_list_1
#
#
# def Get_friendly(n1: list, n2: list):
#     sum_1 = sum(n1)
#     sum_2 = sum(n2)
#     return sum_1, sum_2
#
#
# def Main():
#     numb_1 = int(input("Введи число: "))
#     numb_2 = int(input("Введи число: "))
#     print(Get_friendly(Get_dev(numb_1), Get_dev(numb_2)))
#
#
# Main()
#
#
#


def prompt(msg):
    a = int(input(msg))
    return a


def summarize(number, sum=0):
    for item in range(1, number // 2 + 1):
        if number % item == 0:
            sum += item
    return sum


k = 100000
print(my_list := [i for i in range(k)])
for item in my_list:
    if item == summarize(summarize(item)) and item != summarize(item):
        print(item, summarize(item))
