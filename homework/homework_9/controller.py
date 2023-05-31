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
                pass
            case 3:
                pb = model.get_pb()
                view.print_contact(pb, text.load_error)
            case 4:
                contact = view.input_contact(text.new_contact)
                name = model.add_contact(contact)
                print(view.print_messege())

            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                break
