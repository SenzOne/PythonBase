"""Задача 8:
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*

3 2 4 -> yes
3 2 1 -> no"""


def Is_fault(width, length, num):
    if num % width == 0 or num % length == 0:
        return f'yes'
    else:
        return f'no'


width = int(input("Введи ширину: "))
lenght = int(input("Введи длинну: "))
num = int(input("Введи кол-во кусочков: "))
print(Is_fault(width, lenght, num))
