CONTACTS = {}

def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "No user"
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner

def hello_user():
    return 'How can I help you?'

def unknown_command(command):
    return f'Unknown command: {command}'

def goodbye():
    print('Good bye!')
    return

@input_error
def add_user(name, phone):
    # name, phone = args
    CONTACTS[name] = phone
    return f'User {name} added!'

@input_error
def change_phone(name, phone):
    old_phone = CONTACTS[name]
    CONTACTS[name] = phone
    return f'{name}`s old phone number: {old_phone} has been changed to a new one: {phone}'


def show_all(_):
    result = ''
    for name, phone in CONTACTS.items():
        result += f'Name: {name}, phone: {phone}\n'
    return result

def show_phone(name):
    result = ''
    for phone in CONTACTS.values():
        result = f'{name} phone number is: {phone}'
    return result

