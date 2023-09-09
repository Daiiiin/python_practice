class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))

    def calculate_to_100(self):
        return 100 - int(self.age)


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student(self):
        print("Student ID: " + self.student_id)
        super().display_person()

print("PERSON")
input_name = input("What is your name? ")
input_age = input("How old are you? ")

person_1 = Person(input_name, input_age)
person_1.display_person()
print("You will turn 100 years old in " + str(person_1.calculate_to_100()) + " years")

print("\nSTUDENT")
student_1 = Student(input_name, input_age, "17100772")
student_1.display_student()