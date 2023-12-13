'''Дан список чисел. Определите, сколько в нем встречается различных чисел. '''

from random import randint

list_numbers = []
for i in range(10):
    list_numbers.append(randint(1, 5))

res = set(list_numbers)
print(f'list - {list_numbers} res - {res} count - {len(res)}')
