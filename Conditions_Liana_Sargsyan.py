# 1*. Write a Python program that accepts a word from the user and reverse it.
# userWord = input("Please Enter Any Word: ")
# reversedWord = userWord[::-1]
# print(reversedWord)

# 2. Write a Python program to count that user inputted number is even or odd.
# num = int(input("Please Enter Some Number: "))
# evenOddChecking = num % 2
# if evenOddChecking == 0:
#     print(f"{num} is an odd number")
# else:
#     print(f"{num} is an even number")

# # 3.Write a Python program to find is inputted number in 100 to 400 (both included). Hint (don't google task description)
# num = int(input("Enter some number: "))
# if num >= 100 and num <= 400:
#     print(f"{num} is in 100-400 interval")
# else num < 100 or num > 400:
#     print(f"{num} is not in 100-400 interval")

# 4. Write a Python program that get 2 numbers from user and return Biggest, Median, Sum, Multiply, Divide and Subtract
# num1 = int(input("Number 1 is:"))
# num2 = int(input("Number 2 is:"))
# if num1 > num2:
#     print("Number 1 is the biggest number")
# elif num1 < num2:
#     print("Number 2 is the biggest number")
# sumResult = num1 + num2
# print(f"{num1} + {num2} =", sumResult)
# medianResult = (num1 + num2) / 2
# print("The median of two numbers equals to", medianResult)
# multiplicationResult = num1 * num2
# print(f"{num1} * {num2} =", multiplicationResult)
# divisionResult = num1 / num2
# print(f"{num1} / {num2} =", divisionResult)
# subtractionResult = num1 - num2
# print(f"{num1} - {num2} =", subtractionResult)

# # 5. Write a Python program to get next day of a given date.
# # 	Expected Output:
# #
# 	Input a year: 2016
# 	Input a month [1-12]: 8
# 	Input a day [1-31]: 23
# 	The next date is [yyyy-mm-dd] 2016-8-24
year = int(input("Input a year:"))
month = int(input("Input a month [1-12]:"))
day = int(input("Input a day [1-31]:"))

if year % 400 == 0:
    leapYear = True
elif year % 100 == 0:
    leapYear = False
elif year % 4 == 0:
    leapYear = True
else:
    leapYear = False
if month in [1, 3, 5, 7, 8, 10, 12]:
    monthLen = 31
elif month in [4, 6, 9, 11]:
    monthLen = 30
elif month == 2:
    if leapYear:
        monthLen = 29
    else:
        monthLen = 28
# elif month in [1,2,3,4,5,6,7,8,9,10,11,12]:
#     monthLen <= 31
    print("Error. You have inputted invalid data")
elif month == 12:
    print(year + 1)
if day < monthLen:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print(f"The next date is [yyyy-mm-dd]", year, "-", month, "-", day, sep="")
