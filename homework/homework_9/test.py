data = [{'name': 'Панферова Т.П.', 'phone': '957-04-70 14', 'adress': 'квартал, дом 1, кв. 57'},
        {'name': 'Сухарникова П.Г.', 'phone': '957-08-57', 'adress': '14 квартал, дом 1, кв. 18'},
        {'name': 'Струихина А.П.', 'phone': '957-09-76', 'adress': '14 квартал, дом 1, кв. 32'}]

fnd = str(input("Поиск: "))


for i in data:
    if i['name'][:len(fnd)] == fnd:
        print(f'{i["name"]} = {fnd}')

# def find_contact_successful(data: dict[str, str]):
#     return f'Контакт {data["name"]} {data["phone"]} успешно найден '
#
#
# data = {'name': 'Панферова Т.П.', 'phone': '957-04-11 ', 'adress': '14 квартал, дом 1, кв. 57'}
#
#
# print(find_contact_successful(data))
