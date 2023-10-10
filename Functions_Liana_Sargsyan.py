# 1. Write a function to multiply all the numbers in a given list.
def multiply_numbers(myList):
   result = 1
   for i in myList:
      result = result * i
   return result
myList = [5,6,8,4,1,3]
print(f"The list is: {myList}")
print("The result of multip"
      "l`ication is: ", multiply_numbers(myList))

# 2. Write a function that takes a list and returns a new list with unique elements of the first list
def unique_elements():
  firstList = [1, 1, 5, 8, 4, 8, 6, 9, 3, 4]
  print("The original list is: ", firstList)
  secondList = []
  for i in firstList:
    if i not in secondList:
      secondList.append(i)
  return secondList

print("The new list with unique elements: ", unique_elements())

# 3. Write a function to print the even numbers from a given list.
def even_numbers(myList):
    result = []
    for i in myList:
      if i % 2 == 0:
        result.append(i)

    return result

myList = [15, 26, 37, 48, 55, 69, 80]
print("The even numbers are: ", even_numbers(myList))

# 4. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#       Sample String : 'The quick Brown Fox'
#       Expected Output :
#       No. of Upper case characters : 3
#       No. of Lower case Characters : 12
def upper_lower(sample):
    upper = 0
    lower = 0
    for i in sample:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return upper, lower
sample = "The quick Brown Fox"
print(upper_lower(sample))

# 5. Write a Python function that takes a number as a parameter and check the number is prime or not
def prime_number(num):
    if (num == 1):
        return False
    elif (num == 2):
        return True
    else:
        for i in range(2, num):
            if (num % i == 0):
                return False
        return True


num = int(input("Please input any number: "))
print(prime_number(num))
