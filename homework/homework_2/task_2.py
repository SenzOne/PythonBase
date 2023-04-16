"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа."""
import random
from random import randint

num_1 = random.randint(1, 1001)
num_2 = random.randint(1, 1001)

S = num_1 + num_2
P = num_1 * num_2


def Find_hidden_num(s, p):

    x = 1
    y = s - x
    while x <= s // 2:
        if x * y == p:
            return f'{x} {y}'
        else:
            x += 1
            y = s - x


print(f'Задуманные числа: {num_1} {num_2} найденны: {Find_hidden_num(S, P)}')
