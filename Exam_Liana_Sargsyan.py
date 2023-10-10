# Exercise 1: Write a Python function called calculate_average that takes a list of numbers as input and returns the average (mean) of those numbers. Test your function with the following list: [10, 20, 30, 40, 50].
def calculate_average(myList):
    return sum(myList)/len(myList)

myList = 10, 20, 30, 40, 50
print("The average is", (calculate_average(myList)))
#
# #     listSum = 0
# #     count = 0
# #     for i in myList:
# #         listSum += i
# #         count += 1

# Exercise 2: Create a Python class called Rectangle with two attributes: width and height.
# Implement a method named calculate_area that calculates and returns the area of the rectangle.
# Then, create an instance of the Rectangle class with a width of 5 units and a height of 10 units.
# Calculate and print the area of the rectangle.
class Rectangle():
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight

    def calculate_area(self):
        return self.width * self.hight
rectangle = Rectangle(5,10)
print(rectangle.calculate_area())