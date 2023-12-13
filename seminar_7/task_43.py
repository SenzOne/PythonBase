# Напишите функцию same_by (characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики,
# и возвращают True, если это так. Если значение характеристики для разных объектов
# отличается - то False.
# Для пустого набора объектов, функция должна возвращать Тгце. Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.
import random


def same_by(characteristic, objects):
    return set(list(map(characteristic, objects)))


obj_list = [x * 2 for x in range(1, 11)]
print(obj_list)

print(same_by(lambda x: x % 2 == 0, obj_list))
