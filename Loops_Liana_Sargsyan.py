# 1. Display all tree digits numbers using loops.
for i in range(100, 1000):
    print(i)

# 2. Write a program to display all tree digits even numbers.
for i in range(100, 1000):
    if i % 2 != 0:
        print(i)

# 3. Write a program to display all five digits odd numbers in one line.
for i in range(10000, 99999):
    if i % 2 == 0:
        print(i, end=" ")

# 4. Write a program to display all numbers till 1000, which are divided both by 5 and 7.
for i in range(1, 1000):
    if i % 5 == 0 and i % 7 == 0:
        print(i)

# 5. Write a program to display every third element of the list.
numbers = [5, 9, 14, 99, 5, 78, 36, 100, 99, 1, 35, 78, 45, 31, 14]
for i in numbers[::3]:
    print(i, end=" ")

# 6. Write a program to display only lowercase elements from the list. Note: list contains at least 15 - 20 elements
words = ["happy", "Dog", "blue Dog", "Song", "sad", "Armenia", "cat", "Green", "orange", "Apple", "World", "Lion", "black", "monkey", "Banana"]
for i in words:
    if i == i.lower():
        print(i)

# 7. Write a program to check whether a specified list is sorted or not

myList = [4, 15, 9, 66, 20, 30]
myListCopy = myList.copy()
myListCopy.sort()
while myList == myListCopy:
    print("The list is sorted")
    break
else:
    print("The list is not sorted")

# Or
myList = [5, 15, 9, 66, 20, 30]
i = 0
while i in range(0, len(myList)):
    if myList[i] < myList[i + 1]:
        print("The list is sorted")
        i += 1
else:
    print("The list is not sorted")
    while i in range(0, len(myList)):
        if myList[i] > myList[i + 1]:
            print("The list is sorted")
            i += 1
        else:
            print("The list is not sorted")
