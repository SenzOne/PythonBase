""" Задача 4:
Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
 что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
 чем Петя и Сережа вместе?
*Пример:*

6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10
"""

def Sum_cranes(s):
    cranes_koli = s // 4
    cranes_peti = s // 4
    cranes_kati = s / 1.5
    return f'{cranes_koli} {cranes_peti} {cranes_kati}'


n = int(input("Введи количество журавликов: "))
print(Sum_cranes(n))
