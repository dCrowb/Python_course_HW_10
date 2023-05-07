import argparse
import re


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
        except AttributeError:
            print('Incorect argument!')
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
    contact_book[name] = phone
    result = f'Contact: {name} have been created with phone: {phone}!'
    return result


@input_error
def change_contact(name: str, phone: str):
    if not phone:
        result = 'Wrong phone number. Try again!'
        return result
    old_phone = contact_book[name] 
    contact_book[name] = phone
    result = f'Contact: {name} has been saved with phone: {phone}!'
   
    return result
    
@input_error   
def show_name_contact(phone: str):
    for key, value in contact_book.items():
        if value == phone:
            name = key
    result = f'Contact name: {name}!'
    return name




def end_process():
    mesage = f'Good bye!'
    return mesage


def greeting_user():
    mesage = f'How can I help you?'
    return mesage


@input_error
def show_all_contacts():
    result = ''
    for key, value in contact_book.items():
        result += f'Name: {key:<12}| Phone: {value:^14}|\n' 
    return result


@input_error
def build_parser(arguments: str):
    parser = argparse.ArgumentParser(description="Contact book")
    parser.add_argument("-n", dest="name")
    parser.add_argument("-p", dest="phone")
    args = parser.parse_args(arguments.split())
    return args


def command_parser(user_input: str):
    command_elements = user_input.split(' ', 1)
    if len(command_elements) < 2:
        arguments = None
    else:
        arguments = user_input.split(' ', 1)[1]
    parsed_args = build_parser(arguments)
    return command_elements[0], parsed_args


def main():
    '''---------------------------
        add -n [name] -p [phone] - add new contact.
        change -n [name] -p [phone]- change existing contact.
        phone -n [name] - show number.
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
        elif command in COMMAND_TWO_ARGUMENTS:
            print(COMMANDS[command](arguments.name, arguments.phone))
        elif command == 'phone':
            print(COMMANDS[command](arguments.phone))
        else:
            print('Wrong command! Try again!')


END_COMMAND = ['good_bye', 'exit', 'close', '.']
COMANDS_WITHOUT_ARGUMENTS = ['show_all', 'hello']
COMMAND_TWO_ARGUMENTS = ['add', 'change']
COMMANDS  = {'add': add_contact,
            'change': change_contact,
            'phone': show_name_contact,
            'show_all': show_all_contacts,
            'hello': greeting_user
            }

if __name__ == '__main__':
    contact_book = {}
    main()