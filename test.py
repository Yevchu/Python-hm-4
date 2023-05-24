user = {
    'vit': '123',
    'petro': '234',
    'alexa': '567',
    'Alice': '1234567890',
    'Bob': '0987654321'
}


# def search_contact_book(contact_book: dict, query: str) -> str:
#     results = ''
#     for name, record in contact_book.items():
#         list_rec = contact_book.values()
#         if query in list_rec or query in contact_book.get(name):
#             results += name + ' ' + record
#     return results


def search_contact_book(contact_book: dict, query: str) -> str:
    result = ''
    try:
        int(query)
        for name, record in contact_book.items():
            if query in contact_book.get(name):
                result += f'User: {name}, {record}\n'
    except ValueError:
        get_user = list(filter(lambda x: query.lower() in x.lower(), contact_book.keys()))
        for name in get_user:
            user_info = user.get(name)
            result += f'User: {name}, {user_info}\n'
    return result
print(search_contact_book(user, '1')) 
