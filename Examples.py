# 1.Example 1: Treating the functions as objects.
# def yell(text):
#     return text.upper()
#
# print (yell("hello"))
#
# bark = yell
# print(bark("woof"))
# print(id(yell))
# print(id(bark))









# 2.Example 2: Passing the function as an argument
# def yell(text):
#     return text.upper()
# def greet(func):
#     greeting = func("Hi, I am created by a function passed as an argument")
#     print(greeting)
#
# greet(bark)







# 3.Nested/Inner functions
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()




# 4. Returning Functions From Functions
# def parent(name):
#     def first_child():
#         return "Hi, I am the first child"
#
#     def second_child():
#         return "Hi, I am the second child"
#
#     if name == "Anna":
#         return first_child
#     else:
#         return second_child
# name = "John"
# print(parent(name))



# def reverse_word():
#     userWord = input("Please Enter Any Word: ")
#     reversedWord = userWord[::-1]
#     print(reversedWord)
#
# reverse_word()