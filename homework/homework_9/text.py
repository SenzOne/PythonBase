main_menu = '''\nГлавное меню:
        1. Открыть файл
        2. Записать файл
        3. Показать всю телефонную книгу
        4. Добавить контакт
        5. Найти контакт
        6. Изменить контакт
        7. Удалить контакт
        8. Выход\n'''

imput_choice = 'Выбирите пункт меню: \n'
load_successful = 'Телефонная книга открыта'
save_successful = 'Телефонная книга успешно сохранена'
load_error = 'Телефонная книга пуста или не открыта'
input_contact = {'name': 'Введите имя: ',
                 'phone': 'Введите телефон: ',
                 'adress': 'Введите адрес: '}
error_del_contact = 'Контакта с таким индексом нет'
index_del_contact = 'Введите индекс контакта, который хотите удалить: '
index_change_contact = 'Введите индекс контакта, который хотите изменить: '
new_contact = 'Введите данные нового контакта (пустое поле для отмены): '
cancel_input = 'Отмена ввода'
search_name = 'Кого найти?: '
search_phone = 'Введите номер : '
search_error = 'Такого контакта нет'


def new_contact_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен'


def del_contact(name: str):
    return f'Контакт {name} успешно удален'


def chenge_contact_text(data: str):
    new_data = str(input(f'Изменить "{data}" на -> : '))
    return new_data


def chenge_contact_successful(name: str) -> str:
    return f'Контакт {name} успешно изменен'


def find_contact_successful(data: dict[str, str]):
    return f'Контакт {data["name"]} {data["phone"]} успешно найден '

