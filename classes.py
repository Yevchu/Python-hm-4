from collections import UserDict

class Field:
    def __init__(self, value) -> None:
        self.value = value 
    
    def __str__(self) -> str:
        return f'{self.value}'

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name: Name) -> None:
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)
    
    def remove_phone(self, phone):
        self.phones.remove(phone)

    def change_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record
