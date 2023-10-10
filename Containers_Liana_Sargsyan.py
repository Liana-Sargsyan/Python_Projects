#  1. Write a Python program to get the largest number from a list.
numbers = [45, 89, 100, 15, 7, 31]
largestNumber = max(numbers)
print("The largest number in the list is:", largestNumber)
#
#  2. Write a Python program to check a list is empty or not.
myList = [5, True, "hi", 8.5]
if len(myList) == 0:
    print("The list is empty")
else:
    print("The list is not empty")
#
# 3. Write a Python program to remove all elements from a given set.
mySet = {15, 20, 36, 95, 47}
print(f"Original set {mySet}")
mySet.clear()
print(f"Result after clear: {mySet}")
#
#  4. Write a Python program to check if a given value is present in a set or not.
colors = {"blue", "red", "orange", "green"}
if "blue" in colors:
    print("The set contains given value")
else:
    print("The set does not contain given value")
# OR
print("blue" in colors)
print("white" in colors)
#
#  5. Write a Python program to convert a list to a tuple.
animals = ["cat", "dog", "lion", "rabbit", "wolf"]
print(f"Original list {animals}")
print(type(animals))
tupleAnimals = tuple(animals)
print(f"List after convert to a tuple {tupleAnimals}")
print(type(tupleAnimals))
#
# # 6. Write a Python program to remove an item from a tuple.
myTuple = (25, 18, 85, 106, 97)
print(f"Original tuple is: {myTuple}")
tupleToList = list(myTuple)
tupleToList.remove(25)
print(f"After removing an item: {tupleToList}")
#
# # 7. Write a Python script to check whether a given key already exists in a dictionary or not.
myDict = {
 "subject": "Math",
  "class": 9,
  "testing": True
}
if "subject" in myDict:
    print("The key is already exists in a dictionary")
else:
    print("The key doesn't exist in a dictionary")

# 8. Write a Python script to merge two Python dictionaries.
dict1 = {"Armenia": ["Yerevan", "Gyumri", "Vanadzor", "Goris"]}
dict2 = {"Russia": ["Moscow", "Saint Petersburg", "Yekaterinburg", "Volgograd"]}
dict1.update(dict2)
print(f"The two merged dictionaries: {dict1}")

# 9.
myList = ["Anna", "Ani", "Karen", "Garik", "Liana"]
Input1 = input("Please enter any name:")
Input2 = input("Please enter any name:")
print(f"Original list of names is: {myList}")
print(f"The inputted names are: {Input1}, {Input2}")
myList.insert(0, Input1)
myList.append(Input2)
print(f"The list after items insert and append: {myList}")

myTuple = (25, 16, 87, 100, 95)
count = myTuple.count(16)
print(f"The number of specified value is {count}")

mySet = {"blue", "yellow", "orange", "green"}
print(f"Original version: {mySet}")
mySetUpper = {"blue".upper(), "yellow", "orange", "green".upper()}
print(f"Version after upper case: {mySetUpper}")

myDict = {"Brands": ["Chanel", "OffWhite", "Zara", "Dior"],
          "Subjects": ["Math", "English", "History", "Biology"]}
print(f"Original version of dictionary: {myDict}")
myDict.update({"Years": [1965, 1987, 1957]})
print(f"Dictionary after update: {myDict}")
