class Animal:
    def speak(self):
        print("The animal speaks")

    def move(self):
        print("The animal moves")

class Dog:
    def __init__(self):
        self.animal = Animal()

    def speak(self):
        self.animal.speak()

    def move(self):
        self.animal.move()

# Приклад використання класів
dog = Dog()
dog.speak()  # Виведе: The animal speaks
dog.move()   # Виведе: The animal moves