class UserType:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class PhoneNumber:
    def __init__(self, phone_code, phone_number):
        self.phone_code = phone_code
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.phone_code}{self.phone_number}"

class User:
    def __init__(self, name, age, user_type, phone_number):
        self.name = name
        self.age = age
        self.user_type = user_type
        self.phone_number = phone_number

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Type:", self.user_type)
        print("Phone:", self.phone_number)

# Приклад використання класу
engineer_type = UserType("Engineer")
phone_number = PhoneNumber("050", "9379992")
user = User("John", 25, engineer_type, phone_number)
user.print_details()