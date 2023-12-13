"""
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
"""

n = 'qwerty'
print(n)

my_str = ""


def Revers(s: str):
    if len(s) == 1:
        return s
    return s[-1] + Revers(s[:-1])


print(Revers(n))
