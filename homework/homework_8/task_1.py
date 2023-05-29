# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# 1. Открыть файл +
# 2. Сохранить файл
# 3. Показать тк +
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

file = 'phone_book.txt'


def show_all():
    with open(file, 'r+', encoding='UTF-8') as file_1:
        return file_1.read()


def add_contact():
    with open(file, 'a', encoding='UTF-8') as data:
        name = str(input('Введи имя: ')).capitalize()
        surname = str(input('Введи фамилию: ')).capitalize()
        phone = str(input('Введи тел.: '))
        new_contact = f'{name} {surname} {phone}\n'
        data.writelines(new_contact)
    return 'Контакт добавлен'


def clear_all():
    with open(file, 'w', encoding='UTF-8') as data:
        data.write('')
        answ = str(input('Удалить все данные? y/n'))
    return 'Все данные удалены' if answ == 'y' else 'Данные не удалены'


def faind_contact():
    data_list = show_all().split('\n')
    name = str(input('Кого найти?: ')).capitalize()
    for i in data_list:
        res = i.split()
        if res[0] == name:
            return i
    else:
        return 'Такого имени нет'


def change_contact():
    data_list = show_all()
    tardet = faind_contact()
    new_data = str(input('Новое значение: '))
    new_file = data_list.replace(tardet, new_data)

    with open(file, 'w', encoding='UTF-8') as file_2:
        file_2.write(new_file)
    return f'Вы заменили {tardet} на {new_data}'


def main_func():
    print('1 - показать всю книгу ')
    print('2 - добавить контакт')
    print('3 - найти контакт')
    print('4 - изменить контакт')
    print('5 - удалить контакт')
    print('6 - закрыть книгу')
    print('8 - очистить книгу')

    while True:
        menu = int(input('Действие: '))
        if menu == 1:
            print(show_all())
        elif menu == 2:
            print(add_contact())
        elif menu == 3:
            print(faind_contact())
        elif menu == 4:
            print(change_contact())
        elif menu == 6:
            break
        elif menu == 8:
            print(clear_all())


main_func()

