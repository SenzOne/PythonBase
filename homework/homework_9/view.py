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
