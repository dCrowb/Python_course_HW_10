import json
import re

END_FLAGS = ['good bye', 'close', 'exit', '.']
OPERATIONS = ['add', 'change', 'phone', 'show all']
operation_two_parameters = ['add', 'change']
operation_one_parameters = ['phone']

def check_phone_number(phone: str):
    phone = phone.replace(' ', '').replace('-', '')
    check_phone = re.search(r'[+][0-9]{12}|[0-9]{10}', phone)
    if check_phone and (len(phone) == 13 or len(phone) == 10):
        return phone
    else:
        return None


def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except ValueError:
            print('Give me name and phone please')
        except KeyError:
            print('User doesn`t exist')
        except IndexError:
            print('Enter user name')
        except UnboundLocalError:
            print('Try again')
    return inner


def command_parser(user_command: str):
    command_elements = []
    check_command = user_command.split(' ', 1)
    if check_command[0] in ['show'] :
        check_command = user_command.split()
        command_elements.append(user_command) if len(check_command) == 2 else command_elements.append('Error')
    elif check_command[0] in operation_two_parameters:
        command, arguments = check_command
        name = arguments.split(' ', 1).pop(0)
        phone = arguments.split(' ', 1).pop(1)
        phone = check_phone_number(phone)
        command_elements = [command, name, phone]
    elif check_command[0] in operation_one_parameters:
        command, argument = check_command
        phone = check_phone_number(argument)
        command_elements = [command, phone]
    else:
        command_elements = ['Error']
    print(command_elements)
    return command_elements


def end_process():
    with open('./contact_book.json', 'w') as file:
        json.dump(contact_book, file)
    
    return False


def greeting_func():
    print('How can I help you?')


@input_error
def add_contact(name, phone):
    if not phone:
        result = 'Wrong phone number. Try again!'
        return result
    contact_book[name] = phone
    result = f'Contact: {name} have been created with phone: {phone}!'
    return result

@input_error
def change_contact(name, phone):
    if not phone:
        result = 'Wrong phone number. Try again!'
        return result
    old_phone = contact_book[name] 
    contact_book[name] = phone
    result = f'Contact: {name} has been saved with phone: {phone}!'
    return result
    
@input_error   
def show_name_contact(phone):
    for key, value in contact_book.items():
        if value == phone:
            name = key
    result = f'Contact name: {name}!'
    return name


@input_error
def show_all_contact():
    result = ''
    for key, value in contact_book.items():
        result += f'Name: {key:<12}| Phone: {value:^14}|\n' 
    return result
         

def main_controller(user_command: str):
    command_elements = command_parser(user_command)
    command = command_elements[0]
    if command == 'add':
        name, phone = command_elements[1:]
        result = add_contact(name, phone)
        return result
    elif command == 'change':
        name, phone = command_elements[1:]
        result = change_contact(name, phone)
        return result
    elif command == 'phone':
        phone = command_elements[1]
        result = show_name_contact(phone)
        return result
    elif command == 'show all':
        result = f'Full contact list:\n{show_all_contact()}'
        return result
    else:
        result = 'Wrong command. Try again!'
        return result
    
    
def main():
    '''---------------------------
        add [contact] [phone] - add new contact.
        change [contact] [phone]- change existing contact.
        phone [contact] - show number.
        show all - show all stored contacts and their numbers.
        To terminate the program, enter one of the following commands:
        good bye
        close
        exit
        \n---------------------------'''
    process_status = True
    while process_status:
        user_command = input('\nWait for command!\nTry "help" for more options.\n____________________________\nInput #: ').lower()
        if user_command in END_FLAGS:
            print('Good bye!')
            process_status = end_process()
        elif user_command == 'help':
            help(main)
        elif user_command == 'hello':
            greeting_func()
        else:
            result = main_controller(user_command)
            result and print(result)


if __name__ == '__main__':
    with open('./contact_book.json', 'r') as file:
        contact_book = json.load(file)
    print(contact_book)
    main()
