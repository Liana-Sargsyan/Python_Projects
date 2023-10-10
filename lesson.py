# num1 = int(input("Number 1 is:"))
# num2 = int(input("Number 2 is:"))
#
# if num1 > num2:
#     print("Number one is greater then number two")
# elif num1 < num2:
#     print("Number one is smaller then number two")


# name = "John Smith"
# print(name[3])
# print(name[-7])

# word = "gurguremgy"
# print(word[0])
# print(word[3])
# print(word[8])
# print(word[-2])
# print(word[-7])
# print(word[-10])
#
# name = "Liana Sargsyan Stepan"
# # print(name[:5])
# # print(name[6:14:])
# # print(name[-6:])
#
# print(name[6:14:-1])

# password = input("Please enter  your password:(min 20 character):")
# if len(password) >= 20:
#     print(password[::-1])
# else len(password)
#     print("Your text is shorter")

# text = input("Please enter some text:")
# print (len(text))
# if len(text) % 2 == 0:
#     print(text[::-1])
# else:
#     print(text[::2])

# name = "liana S a r g sy "
# x = slice(1, 5)
# print(name[x])
# myset1 = {"anna", "vardan", "shushan"}
# myset2 = {1,3,5,6}
# myset1 = set.union(myset2)
# print(myset1)
# listx = ["cat", "dog", "lion", "rabbit", "wolf"]
# print(listx)
# print(type(listx))
# #use the tuple() function built-in Python, passing as parameter the list
# tuplex = tuple(listx)
# print(tuplex)
# print(type(listx))

# myDict = {"Fruits": ["apple", "orange", "peach", "pear", "banana"],
#           "Vegetables": ["tomato", "cucumber", "carrot", "cabbage"],
#           "Berries": ["raspberry", "watermelon", "melon", "blueberry"]}
# print(myDict)

# myList = ["Anna", "Ani", "Karen", "Garik", "Liana"]
# Input1 = input("Please enter any name:")
# Input2 = input("Please enter any name:")
# print(f"Original list of names is: {myList}")
# print(f"The inputted names are: {Input1}, {Input2}")
# myList.insert(0, Input1)
# myList.append(Input2)
# print(f"The list after items insert and append: {myList}")

# myTuple = (25, 16, 87, 100, 95)
# count = myTuple.count(16)
# print(f"The number of specified value is {count}")

# mySet = {"blue", "yellow", "orange", "green"}
# print(f"Original version: {mySet}")
# mySetUpper = {"blue".upper(), "yellow", "orange", "green".upper()}
# print(f"Version after upper case: {mySetUpper}")

# myDict = {"Brands": ["Chanel", "OffWhite", "Zara", "Dior"],
#           "Subjects": ["Math", "English", "History", "Biology"]}
# print(f"Original version of dictionary: {myDict}")
# myDict.update({"Years": [1965, 1987, 1957]})
# print(f"Dictionary after update: {myDict}")

# userWord = input("Please enter any word:")
# reverseUserWord = userWord[:: -1]
# print(reverseUserWord)
# if userWord == reverseUserWord:
#     print("The word is palindrome")
# else:
#     print("The word is not palindrome")

# userNumber = input("Please enter any number:")
# reverseUserNumber = userNumber[::-1]
# if userNumber == reverseUserNumber:
#     print("The number is palindrome")
# else:
#     print("The number is not palindrome")

# input1 = int(input("Please input first number:"))
# input2 = int(input("Please input second number:"))
# input3 = int(input("Please input third number:"))
# # averageResult = (input1 + input2 + input3) / 3
# # print(f"The average result is: {averageResult}")
# if input1 > input2 and input2 {} input3:
#     print("Number 2 is the mean")

# i = 0
# while i < 10:
#     if i == 6:
#         continue
#     i += 1
#     print(i)
#     i += 1

# i = 0
# while i < 10:
#     if i == 6:
#         break
#     # i += 1
#     print(i)
#     i += 1
#
# # myList = [3, 5, 1, 7, 6, 3]
# # resultList = []
# # for i in myList:
# #     resultList.append(i ** 2)
#
# # i = 1
# # while 100 < i < 1000:
# #     print(i)
# #     i += 1
#
# # myList = [5, 15, 9, 66, 20, 30]
# # i = 0
# # while i in range(0, len(myList)):
# #     if myList[i] < myList[i + 1]:
# #         print("The list is sorted")
# #         i += 1
# # else:
# #     print("The list is not sorted")
# #     while i in range(0, len(myList)):
# #         if myList[i] > myList[i + 1]:
# #             print("The list is sorted")
# #             i += 1
# #         else:
# #             print("The list is not sorted")
#
# class Animals():
#     def __init__(self, name, type, legs, color):
#         print("Called Constructor")
#         self.name = name
#         self.type = type
#         self.legs = legs
#         self.color = color
#
#     def eat(self):
#         print("Eating")
#
#     def sleep(self):
#         print("Sleeping")
#
#     def sound(self):
#         print("Sounds")
#
#     def movement(self):
#         print("Movement")
#
#
#     def get_basic_characteristics(self):
#         return [self.name, self.type, self.color, self.legs]
# shark = Animals("shark", "fish", 0, "white")
# print("The name is:", shark.name, "/", "The type is:", shark.type, "/", "Legs =", shark.legs, "/", "The color is:", shark.color)
# shark.movement()
# shark.eat()
# shark.sleep()
# class WildAnimals(Animals):
#     def __init__(self,name, type, legs, color, hunting):
#         super().__init__(name, type, legs, color)
#         self.hunting = hunting
#
#
#     def hunting_behavior(self):
#         print(f"Wolves are hunting on {self.hunting}")
#
#     def get_basic_characteristics(self):
#         super().get_basic_characteristics()
#         print(super().get_basic_characteristics())
#         print("Hunting....")
#     #
#     # def __add__(self, other):
#     #     print(Animals(self.legs) + WildAnimals(self.legs))
#
#
# Wolf = WildAnimals("wolf", "mammel", 4, "grey", "animals")
# Wolf.get_basic_characteristics()
# Wolf.hunting_behavior()
# class DomesticAnimals(Animals):
#     def __init__(self, name, type, legs, color, feeding):
#         super().__init__(name, type, legs, color)
#         self.feeding = feeding
#
#     def how_to_feed_an_animal(self):
#         print(f"Cows are eating {self.feeding}")
#
#
#     def get_basic_characteristics(self):
#         super().get_basic_characteristics()
#         print("Feeding...")
#
# Cow = DomesticAnimals("cow", "mammel",4, "Black and White", "grass")
# Cow.how_to_feed_an_animal()

# def my_decorator(func):
#     def wrapper():
#         func()
#         print("Start")
#
#     return wrapper
#
# @my_decorator
# def my_function():
#     print("Hello. I am the decorated function")
# my_function()


# size = 8
# for i in range(size):
#     print("*" * size)

for i in range (1, 9, +1):
    for i in range (1,9,+1):
        print("*", end = " ")
    print()

# size = 8
# for i in range(size):
#     for j in range(size):
#         print("* ", end="")
#     print("\n")

