from collections import UserDict

class Field:
    def __init__(self, value) -> None:
        self.value = value 

class Name(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

    def __repr__(self) -> str:
        return f"{self.value}"

class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

    def __repr__(self) -> str:
        return f"{self.value}"
class Record:
    
    def __init__(self, name: Name, phone: Phone | None=None) -> None:
        self.name = name
        self.phones = []
        if phone is not None:
            self.add_phone(phone)

    def add_phone(self, phone: Phone | str):
        if isinstance(phone, str):
            phone = self.create_phone(phone)
        self.phones.append(phone)
    
    def create_phone(self, phone: str):
        return Phone(phone)

    def remove_phone(self, phone):
        new_phone_list = filter(lambda x: str(x) != str(phone), self.phones)
        return list(new_phone_list)
        # for p in self.phones:
        #     new_phone_list = []
        #     if p.value != phone:
        #         new_phone_list.append(p) 

        #     return new_phone_list

    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                print(f'{old_phone} has been changed to a new one: {new_phone}')
                return phone
            else:
                print('Phone not found')
    
    def show(self):
        res = ''
        for index, phone in enumerate(self.phones):
           res += f'{index + 1}. {phone.value} '
        return res

    def __repr__(self) -> str:
        return f'{self.phones}'
class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def show(self) -> str:
        res = ''
        for name, phones in self.data.items():
            res += f'User: {name} have phone: {phones.show()}\n'
        return res

    def get_records(self, name: str) -> Record:
        return self.data[name]
