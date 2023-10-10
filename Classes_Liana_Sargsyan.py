# 1. Class of Animal
class Animals():
    name = None
    type = None
    legs = None
    color = None
    def __init__(self, name, type, legs, color):
        print("Called Constructor")
        self.name = name
        self.type = type
        self.legs = legs
        self.color = color

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

    def sound(self):
        print("Sounds")

    def movement(self):
        print("Movement")


    def get_basic_characteristics(self):
        return [self.name, self.type, self.color, self.legs]

shark = Animals("shark", "fish", 0, "white")
print("The name is:", shark.name, "/", "The type is:", shark.type, "/", "Legs =", shark.legs, "/", "The color is:", shark.color)
shark.movement()
shark.eat()
shark.sleep()
pig = Animals("pig", "mammal", 4, "black")
print("The name is:", pig.name, "/", "The type is:", pig.type, "/", "Legs =", pig.legs, "/", "The color is:", pig.color)
pig.sound()
pig.eat()

# 2. Class of Student

class Student():
    name = None
    ID = None
    GPA = None
    faculty = None

    def __init__(self, name, ID, GPA, faculty):
        print("Called Constructor")
        self.name = name
        self.ID = ID
        self.GPA = GPA
        self.faculty = faculty


    def study(self):
        print("Student is studying: ", self.get_personal_information())

    def read(self):
        print("Student is reading")

    def write(self):
        print("Student is writing")

    def preparing_for_exams(self):
        print("Student prepares for exams")

    def get_personal_information(self):
        return self.faculty

student1 = Student("Arman", 587, 18.5, "Economics")
print("Name is:", student1.name, "/", "Id:", student1.ID, "/", "GPA =", student1.GPA)
student1.study()
student1.preparing_for_exams()
student1.write()
student1.read()
student2 = Student("Lilit", 549, 16.4, "History")
print("Name is:", student1.name, "/", "Id:", student1.ID, "/", "GPA =", student1.GPA)
student1.study()
student1.preparing_for_exams()
student1.write()
student1.read()

# 3. Math.ceil Function
import math
number = int(input("Please input any number: "))
print(math.ceil(number))
