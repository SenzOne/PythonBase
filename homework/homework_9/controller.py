import view
import model
import text


def start():

    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_pb()
                view.print_messege(text.load_successful)
            case 2:
                model.save_pb()
                view.print_messege(text.save_successful)
            case 3:
                pb = model.get_pb()
                view.print_contact(pb, text.load_error)
            case 4:
                contact = view.input_contact(text.new_contact, text.cancel_input)
                name = model.add_contact(contact)
                view.print_messege(text.new_contact_successful(name))

            case 5:
                pass
            case 6:  # Изменить контакт
                pb = model.get_pb()
                index = view.input_index(text.index_change_contact, pb, text.load_error)
                data = model.chenge_contact(index)  # data -> {'name': 'Панферова Т.П.', 'phone': '957-04-70 14', ... }
                new_data = view.chenge_contact(data)
                name = model.add_contact(new_data)
                view.print_messege(text.chenge_contact_successful(name))

            case 7:
                pb = model.get_pb()
                index = view.input_index(text.index_del_contact, pb, text.load_error)
                name = model.del_contact(index)
                view.print_messege(text.del_contact(name))

            case 8:
                break
