import re
from datetime import datetime

def validate_booking_form(name,passport_no, ph_no, email,depart_date, pay_method):

    if not re.fullmatch(r'[A-Za-z]+(?:\s[A-Za-z]+)*', name):
        return "Invalid name!"
    
    if not re.fullmatch(r'[A-Za-z0-9]{9}', passport_no):
        return "Invalid passport number! Must be 9 alphanumeric values long "
    
    if not re.fullmatch(r'\d{10}', ph_no):
        return "Invalid phone number!"
    
    if not re.fullmatch(r'[A-Za-z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-Z0-9]+$', email):
        return "Invalid Email !"
    
    try :
        datetime.strftime(depart_date, '%d%m%Y')
    except ValueError:
        return "Departure date must be in format dd/mm/yyyy"
    
    if pay_method.lower() not in ['credit', 'debit', 'netbanking']:
        return "Invalid payment method! Use credit debit or netbanking only"
    
    return "All INputs are valid"

name = input("Enter name: ")
passport_number = input("Enter passport number: ")
phone  = input("Enter phone number : ")
email = input("Enter email: ")
departure_date = input("Enter data of dearture in format (dd/mm/yyyy): ")
payment = input("Choose payment method(credit, debit, netbanking):   ")

print(validate_booking_form(name, passport_number, phone, email, departure_date, payment))