"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
 чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
 которые нужно перевернуть"""
import random
from random import randint


def Get_money(n):
    coins_list = []
    for i in range(n):
        coins_list.append(random.randint(0, 1))
    return coins_list


def Coin_flip(coins_list):
    if sum(coins_list) > len(coins_list) / 2:
        return len(coins_list) - sum(coins_list)
    else:
        return sum(coins_list)


n = int(input("Введи кол-во монет: "))
for i in range(10):
    res = Get_money(n)
    print(f'{res} -> {Coin_flip(res)}')
