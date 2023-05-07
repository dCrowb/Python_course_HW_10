import argparse
import re
import classes


class PhoneError(Exception):
    pass


def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except SystemExit:
            print('Incorect command')
        except PhoneError:
            print('Incorrect phone number')
        # except AttributeError:
        #     print('Incorect argument!')
        except ValueError:
            print('Give me name and phone please')
        except KeyError:
            print('User doesn`t exist')
        except IndexError:
            print('Enter user name')
        except UnboundLocalError:
            print('Try again')
    return inner


@input_error
def check_phone_number(phone: str):
    phone = phone.replace(' ', '').replace('-', '')
    check_phone = re.search(r'[+][0-9]{12}|[0-9]{10}', phone)
    if check_phone and (len(phone) == 13 or len(phone) == 10):
        return phone
    else:
        raise PhoneError


@input_error
def add_contact(name: str, phone: str):
    if not phone:
        result = 'Wrong phone number. Try again!'
        return result
    elif name in contact_book.data.keys():
        result = 'This contact exist in "Address book". Use change command!'
    else:
        contact_book.add_record(name, phone)
        result = f'Contact: {name} have been created with phone: {phone}!'
        return result


@input_error
def remove_phone(name: str, phone: str):
    if not phone:
        result = 'Wrong phone number. Try again!'
        return result
    elif name not in contact_book.data.keys():
        result = f'Contact {name} not found in Address book!'
        return result
    elif name in contact_book.data and phone in contact_book.data[name].get_list_phones():
        contact_book.data[name].remove_phone(phone)
        result = f'Contact {name} has been removed phone: {phone}!'
    return result


@input_error
def replace_phone(name: str, phone: str, new_phone: str):
    if not phone:
        result = 'Wrong phone number. Try again!'
        return result
    elif name not in contact_book.data.keys():
        result = f'Contact {name} not found in Address book!'
        return result
    elif name in contact_book.data and phone in contact_book.data[name].get_list_phones():
        contact_book.data[name].change_phone(phone, new_phone)
        result = f'Contact {name} has been changed phone: {phone} on phone: {new_phone}!'
    return result


@input_error
def change_contact(name: str, phone: str):
    if not phone:
        result = 'Wrong phone number. Try again!'
        return result
    elif name not in contact_book.data.keys():
        result = f'Contact {name} not found in Address book!'
        return result
    elif name in contact_book.data and phone not in contact_book.data[name].get_list_phones():
        print(contact_book.data[name].get_list_phones())
        contact_book.data[name].add_phone(phone)
        result = f'Contact {name} has been added phone: {phone}!'
    elif name in contact_book.data and phone in contact_book.data[name].get_list_phones():
        result = f'Contact: {name} with phone: {phone} already in Address book!'
    return result
    

@input_error   
def show_name_contact(name_phone: str):
    if name_phone in contact_book.data.keys():
        result =  f'Phones{contact_book.data[name_phone].get_list_phones()}'
    else:
        for key, value in contact_book.data.items():
            if name_phone in value.get_list_phones():
                name = key
                result = f'Contact name: {name}!'
            else:
                result = f"Contact with this name or phone doesn't exist in Address book"
    return result


def end_process():
    mesage = f'Good bye!'
    return mesage


def greeting_user():
    mesage = f'How can I help you?'
    return mesage


@input_error
def show_all_contacts():
    result = ''
    for key, value in contact_book.data.items():
        result += f'Name: {key:<12}| Phone: {value.show_all_pnone()}\n' 
    return result


@input_error
def build_parser(arguments: str):
    parser = argparse.ArgumentParser(description="Contact book")
    parser.add_argument("-n", dest="name")
    parser.add_argument("-p", dest="phone")
    parser.add_argument("-r", dest="replace_phone")
    args = parser.parse_args(arguments.split())
    return args


def command_parser(user_input: str):
    command_elements = user_input.split(' ')
    if len(command_elements) < 2:
        arguments = None
        return command_elements[0], arguments
    else:
        arguments = user_input.split(' ', 1)[1]
        parsed_args = build_parser(arguments)
        return command_elements[0], parsed_args


def main():
    '''---------------------------
        add -n [name] -p [phone] - add new contact.
        change -n [name] -p [phone]- change existing contact.
        remove -n [name] -p [phone]- remove existing phone.
        phone -n [name] - show number or -p [phone] - show name.
        show_all - show all stored contacts and their numbers.
        To terminate the program, enter one of the following commands:
        good_bye
        close
        exit
        \n---------------------------'''

    while True:
        user_input = input('\nWait command #:').lower()
        command, arguments = command_parser(user_input)

        if command in COMANDS_WITHOUT_ARGUMENTS:
            print(COMMANDS[command]())
        elif command in END_COMMAND:
            print(end_process())
            break
        elif not arguments:
            print('Wrong command! Try again!')
        elif command in COMMAND_TWO_ARGUMENTS and arguments.replace_phone:
            print(replace_phone(arguments.name, arguments.phone, arguments.replace_phone))
        elif command in COMMAND_TWO_ARGUMENTS:
            print(COMMANDS[command](arguments.name, arguments.phone))
        elif command == 'phone':
            if arguments.phone:
                print(COMMANDS[command](arguments.phone))
            elif arguments.name:
                print(COMMANDS[command](arguments.name))
        else:
            print('Wrong command! Try again!')


END_COMMAND = ['good_bye', 'exit', 'close', '.']
COMANDS_WITHOUT_ARGUMENTS = ['show_all', 'hello']
COMMAND_TWO_ARGUMENTS = ['add', 'change', 'remove']
COMMANDS  = {'add': add_contact,
            'change': change_contact,
            'remove': remove_phone,
            'phone': show_name_contact,
            'show_all': show_all_contacts,
            'hello': greeting_user
            }

if __name__ == '__main__':
    contact_book = classes.AddressBook()
    main()