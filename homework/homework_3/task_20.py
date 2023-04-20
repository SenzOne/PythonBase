"""*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так: A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу,
которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово,
которое содержит либо только английские, либо только русские буквы.
*Пример:*

ноутбук
    12"""

alphabet = [['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
            ['Д', 'К', 'Л', 'М', 'П', 'У', 'D', 'G'],
            ['Б', 'Г', 'Ё', 'Ь', 'Я', 'B', 'C', 'M', 'P'],
            ['Й', 'Ы', 'F', 'H', 'V', 'W', 'Y'],
            ['Ж', 'З', 'Х', 'Ц', 'Ч', 'K'],
            ['Ш', 'Э', 'Ю', 'J', 'X'],
            ['Ф', 'Щ', 'Ъ', 'Q', 'Z']]

cost = [1, 2, 3, 4, 5, 8, 10]


def Create_value():
    big_dict = dict()
    for i in range(len(alphabet)):
        tmp = {letter: cost[i] for letter in alphabet[i]}
        big_dict.update(tmp)
    return big_dict


def Get_value(alphabet_dict, world):
    count = 0
    world = world.upper()
    for letter in world:
        for key, value in alphabet_dict.items():
            if letter == key:
                count += value
                print(f' {key} - {value}')
    return count


def Main():
    alp = Create_value()
    w = str(input("Введи слово на русском или англ: "))
    print(f'В слово - {w} даст {Get_value(alp, w)} очков')


Main()
