
# def days_to_birthday(brth) -> int:
    
#     today = datetime.now().date()
#     birthday = datetime.strptime(brth, '%d-%m-%Y').date()
#     next_bd = birthday.replace(year=today.year)
    
#     if today > next_bd:
#         next_bd = birthday.replace(year=today.year + 1)

#     days_to_birthday = (next_bd - today).days
#     return days_to_birthday

# print(days_to_birthday('29-02-2020'))

from datetime import datetime, date

# contacts = []

def is_leap_year(year):
    # Перевіряємо, чи рік є високосним
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def add_contact(date_string):
    try:
        # Додаємо дату 
        date_obj = datetime.strptime(date_string, '%d-%m-%Y').date()
        current_date = datetime.now().date()

        if (date_obj.month, date_obj.day) == (2, 29) and not is_leap_year(current_date.year):
            date_obj = date_obj.replace(day=date_obj.day - 1)
        birthday = date_obj.replace(year=current_date.year)
        
        if birthday < current_date:
            birthday = birthday.replace(year=current_date.year + 1)
        
        days_to_birthday = (birthday - current_date).days
        
        return days_to_birthday
        
    except ValueError as e:
        print(f"Помилка: {str(e)}")


print(add_contact('29-02-2020'))

contacts = {
    'Vitalic': '19-06-1997'
}


def get_upcoming_birthday(days):
    current_date = datetime.now().date()
    
    upcoming_birthdays = []
    for contact_name, contact_bd in contacts.items():
        date_obj = datetime.strptime(contact_bd, '%d-%m-%Y').date()
        birthday = date_obj.replace(year=current_date.year)
        
        if birthday < current_date:
            birthday = birthday.replace(year=current_date.year + 1)
        
        if (birthday - current_date).days == days:
            upcoming_birthdays.append(contact_name)
    
    return upcoming_birthdays

print(get_upcoming_birthday(16))