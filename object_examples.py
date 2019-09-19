class Company:
    country = "USA"

    def __init__(self, name=None, ceo=None, location=None):
        self.name = name
        self.ceo = ceo
        self.location = location

    @classmethod
    def change_country(cls, country):
        cls.country = country

    def print_argument_value(self):
        print(f"{self.name}, {self.ceo}, {self.location}")


apple = Company('Apple', 'Samarth', 'USA')
microsoft = Company('Microsoft', 'Bill', 'USA')
microsoft.country = 'India'
# print(apple.name)
# print(apple.ceo)
# apple.location = "USA"
# print(apple.location)
apple.print_argument_value()
microsoft.print_argument_value()
print(apple.country)
print(microsoft.country)
print(apple.country)
apple.change_country("India")
print(apple.country)
print(microsoft.country)