import text


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.imput_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def print_messege(messege: str):
    print('\n' + '=' * len(messege))
    print(messege)
    print('=' * len(messege) + '\n')


def print_contact(pb: list[dict[str, str]], err: str):
    if pb:
        print('\n' + '*' * 80)
        for i, contact in enumerate(pb, 1):
            print(f'{i:>3}. {contact.get("name"):<20} | {contact.get("phone"):<20} | {contact.get("adress"):<20}')
        print('*' * 80 + '\n')
    else:
        print_messege(err)


def input_contact(messege: str, cancel: str) -> dict:
    contatc = {}
    for k, v in text.input_contact.items():
        data = input(v)
        if data:
            contatc[k] = data
        else:
            print_messege(cancel)

    return contatc


def input_index(messege: str, pb: list, err: str) -> int:
    while True:
        index = input(messege)
        if index.isdigit() and 0 < int(index) < len(pb) + 1:
            return int(index)
        else:
            print_messege(text.error_del_contact)


def chenge_contact(data: dict[str, str]) -> dict:
    for k, v in data.items():
        data[k] = text.chenge_contact_text(v)
    return data


def find_contact(data: list[dict[str, str]]):
    name = input(str(text.search_name)).lower()
    data_list = []
    for contact in data:
        if contact['name'][:len(name)].lower() == name:
            data_list.append(contact)

    if len(data_list) == 0:
        return print_messege(text.search_error)
    elif len(data_list) == 1:
        return data_list[0]
    else:
        return del_duplicate(data_list)


def del_duplicate(data: list[dict[str, str]], err=None) -> dict:
    print_contact(data, err)
    phone = input(str(text.search_phone)).strip()
    for contact in data:
        if contact['phone'].strip() == phone:
            return contact
        else:
            print(text.search_error)
            return del_duplicate(data, err=None)
