class Library:
    def __init__(self, location=None, no_of_books=None, no_of_staff=None, timing='6AM-9PM', status='Closed', no_of_memebrs=0):
        self.location = location
        self.no_of_books = no_of_books
        self.no_of_staff = no_of_staff
        self.timing = timing
        self.status = status
        self.no_of_members = no_of_memebrs

    def get_library_detail(self):
        details = f"Library is located in {self.location}, it's timing is {self.timing}, their are many books available but record says it has {self.no_of_books}." \
                  f"Right now it is {self.status}. and it visited by {self.no_of_members} people."
        return details

class Librarian:
    def __init__(self, name, qualification, salary, contact_no, working_hour):
        self.name = name
        self.qualification = qualification
        self.salary = salary
        self.contact_no = contact_no
        self.working_hour = working_hour

    # def issued_book(self,number):



class Book:
    def __init__(self, name, author, type, price, availability, number_of_copy):
        self.name = name
        self.author = author
        self.type = type
        self.price = price
        self.availability = availability
        self.number_of_copy = number_of_copy


class Member:
    def __init__(self, name, age, contact_no, address, deposit, borrow_details):
        self.name = name
        self.age = age
        self.contact_no = contact_no
        self.address = address
        self.deposit = deposit
        self.borrow_details = borrow_details
