# 1. Write a program to solve (x + y) * (x + y).
#       Test Data : x = 4, y = 3
#       Expected Output : (4 + 3) ^ 2) = 49
x = 4
y = 3
result = (x + y) ** 2
print("Expected output :", end="")
print("(", x, "+", y, ") ^ 2 =", result, sep="")

# 2. Write a program to parse a string to Float or Integer
var = "555"
var_float = float(var)
print("The result is: ", var_float)


# 3. Given variables x=30 and y=20, write a Python program to print "30+20=50" via variables
x = 30
y = 20
result = x + y
print ("Expected Output:",x, "+", y, "=", result, sep="")

# 4. Write a program to get the Type, and Value of a variable
age = 45
print (type(age))
print (age)


# 5. Write a program to get the volume of a sphere with radius 6
radius = 6
pi = 3.14
volumeOfaSphere = 4/3 *pi* radius**3
print("The volume of a sphere equals to:", volumeOfaSphere)

# myset = {"apple", "orange", "banana"}
# discard = myset.discard(0)
# print(myset)
# # remove = myset.remove("apple")
# # print(myset)
# 6.Write a program to display your details like name, age, address in three different lines
name = "Liana"
age = 32
address = "Armenia, Yerevan"
print(name, age, address, sep="\n")


# 7. Write a program to count the 7% of 500
total = 500
percentage = 7
result = (total * percentage) / 100
print(percentage,"% of", total, "is", result)
