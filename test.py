# user = {
#     'vit': '123',
#     'petro': '234',
#     'alexa': '567',
#     'Alice': '1234567890',
#     'Bob': '0987654321'
# }
import re
# def search_contact_book(contact_book: dict, query: str) -> str:
#     result = ''
#     try:
#         int(query)
#         for name, record in contact_book.items():
#             if query in contact_book.get(name):
#                 result += f'User: {name}, {record}\n'
#     except ValueError:
#         get_user = list(filter(lambda x: query.lower() in x.lower(), contact_book.keys()))
#         for name in get_user:
#             user_info = user.get(name)
#             result += f'User: {name}, {user_info}\n'
#     return result
# print(search_contact_book(user, '1')) 

class Field:
    def __init__(self, value) -> None:
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        self.validator(new_value)
        self.__value = new_value

    def validator(self, value):
        pass
        

class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
 
    def validator(self, new_value):
        if isinstance(new_value, str):
            if not re.match(r'^\+38\d{10}$', new_value):
                print("Phone number should be in the format +380XXXXXXXXX")
                raise ValueError("Phone number should be in the format +380XXXXXXXXX")
        else:
            raise ValueError('value must be str not int')
            
    def __repr__(self) -> str:
        return f"{self.value}"
    

class Name(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

    def __repr__(self) -> str:
        return f"{self.value}"

a = Phone("+380968851771")
b = Name(123)
print(a, b, end='\n')