# 1.  Write a class named Student with two attributes student_id, student_name. Add a new attribute student_class.
#     Create a function to display the entire attribute and their values in Student class.
class Student():

    def __init__(self, student_ID, student_name):
        self.student_ID = student_ID
        self.student_name = student_name

    def new_attribute(self, student_class):
        self.student_class = student_class

    def get_personal_information(self):
        print(f"Student ID is: {self.student_ID}")
        print(f"Student name is: {self.student_name}")
        print(f"Student class is: {self.student_class}")

student1 = Student(1, "Mark")
student1.new_attribute("Biology")
student1.get_personal_information()

# 2. Create a Vehicle class without any variables and methods
class Vehicle():
    pass
# 3. Write a program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle():
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

BMW = Vehicle(130, 20)
print(f"The max_speed of BMW is: {BMW.max_speed}")
print(f"The mileage of BMW is: {BMW.mileage}")

# 4. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)
Bus5 = Bus(70, 12)
print(f"The bus's max_speed is {Bus5.max_speed}")
print(f"The bus's mileage is {Bus5.mileage}")

# 5. Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, bus_seating_capacity):
        super().__init__(max_speed, mileage)
        self.bus_seating_capacity = bus_seating_capacity

    def get_characteristics(self):
        print(f"The speed is: {self.max_speed}. The mileage is: {self.mileage}. The capacity is: {self.bus_seating_capacity}")

Bus10 = Bus(85, 17, 50)
Bus10.get_characteristics()

