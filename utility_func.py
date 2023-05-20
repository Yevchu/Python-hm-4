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
            return 'Missed arguments'
    return inner

def hello_user():
    return 'How can I help you?'

def unknown_command(command):
    return f'Unknown command: {command}'

def goodbye():
    print('Good bye!')
    return 'exit'

@input_error
def add_user(name: str, phone: str) -> str:
    record = Record(Name(name), Phone(phone))
    if name not in CONTACTS.data:
        result = f'New user {name} is added!'
    else:
        return add_phone(name, phone)
    CONTACTS.add_record(record)
    return result

def add_phone(name: str, phone: str) -> str:
    record = CONTACTS.get_records(name)
    record.add_phone(phone)
    CONTACTS.add_record(record)
    return f'For user {name} is added a new phone {phone}!'

@input_error
def change_phone(name, old_phone, new_phone):  #TODO: є проблема з коректністью роботи функції, на даний момент вона працює але в консоль ми отримаємо прінт + None
    record = CONTACTS.get_records(name)
    if not record:
        return "Contact not found"
    record.change_phone(old_phone, new_phone)  
    CONTACTS.add_record(record)
    # return f'{name}`s old phone number: {old_phone} has been changed to a new one: {new_phone}'

def remove_phone(name, phone): # TODO: фукнція працюж не правильно, кінцевий результат залишається без змін, сам рекорд не змінюються, якщо записати рекорд у нову змінну и добавити її в CONTACTS виникає помилка 
    record = CONTACTS.get_records(name)
    if not record:
        return "Contact not found"
    record.remove_phone(phone)
    CONTACTS.add_record(record)
    return f'For {name} phone {phone} is deleted.'

def show_phone(name):
    if name == 'all':
        return show_all()
    else:
        result = ''
        record = CONTACTS.data[name]
        if name:
            result = f'{name} phone number is: {record.show()}'
        else:
            result = f'We dont have {name} in our list'
        return result

def show_all():
    if not CONTACTS:
        return "No contacts found" 
    result = CONTACTS.show()
    return result