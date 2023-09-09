class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))

    def calculate_to_100(self):
        pass


input_name = input("What is your name? ")
input_age = input("How old are you? ")

person_1 = Person(input_name, input_age)
person_1.display_person()