




def add_contact():
    pass


def change_contact():
    pass


def phone_contact():
    mesage = f'Search func'
    return mesage


def end_process():
    mesage = f'Good bye!'
    return mesage


def greeting_user():
    mesage = f'How can I help you?'
    return mesage


def show_all_contacts():
    mesage = contact_book
    return mesage


def command_identify(user_input: str):
    command = user_input.split(' ', 1)[0]
    return command


def command_parser(user_input: str):
    command = user_input.split(' ', 1)[0]
    arguments = user_input.split(' ', 1)[1].strip()
    check_count_arg = arguments.split(' ', 1)
    if len(check_count_arg) == 1 and command in COMMAND_ONE_ARGUMENTS:
        name = arguments
        return name



def main():
    '''---------------------------
        add [contact] [phone] - add new contact.
        change [contact] [phone]- change existing contact.
        phone [contact] - show number.
        show_all - show all stored contacts and their numbers.
        To terminate the program, enter one of the following commands:
        good_bye
        close
        exit
        \n---------------------------'''

    while True:
        user_input = input('\nWait command #:')
        command = command_identify(user_input).lower()
        if command in END_COMMAND:
            print(end_process())
            break
        elif command in COMANDS_WITHOUT_ARGUMENTS:
            print(COMMANDS[command]())
        elif command in COMMAND_ONE_ARGUMENTS:
            arguments = command_parser(user_input)
            mesage = COMMANDS[command](argu)
        else:
            print('Wrong command! Try again!')


END_COMMAND = ['good_bye', 'exit', 'close', '.']
COMANDS_WITHOUT_ARGUMENTS = ['show_all', 'hello' ]
COMMAND_TWO_ARGUMENTS = ['add', 'change']
COMMAND_ONE_ARGUMENTS = ['phone']
COMMANDS  = {'add': add_contact,
            'change': change_contact,
            'phone': phone_contact,
            'show_all': show_all_contacts,
            'hello': greeting_user
            }

if __name__ == '__main__':
    contact_book = []
    main()
