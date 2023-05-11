from classes import AddressBook, Name, Phone, Record
CONTACTS = AddressBook()

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
        except TypeError:
            return 'You missed arguments'
    return inner

def hello_user():
    return 'How can I help you?'

def unknown_command(command):
    return f'Unknown command: {command}'

def goodbye():
    print('Good bye!')
    return

@input_error
def add_user(name: str, phone: str) -> str:
    record = Record(Name(name))
    record.add_phone(Phone(phone))
    CONTACTS.add_record(record)
    return f'User {name} is added!'

@input_error
def change_phone(name, phone):
    record = CONTACTS.data.get(name)
    if not record:
        return "Contact not found"
    old_phone = record.phones[0]
    new_phone = Phone(phone)
    record.change_phone(old_phone, new_phone)
    return f'{name}`s old phone number: {old_phone} has been changed to a new one: {phone}'

def show_all():
    result = ''
    if not CONTACTS:
        return "No contacts found"
    for name, record in CONTACTS.items():
        result += f'Name: {name}, phone: {record.phones[0].value}\n'
    return result

def show_phone(name):
    if name == 'all':
        return show_all()
    else:
        result = ''
        record = CONTACTS.data[name]
        if name:
            result = f'{name} phone number is: {record.phones[0].value}'
        else:
            result = f'We dont have {name} in our list'
        return result

