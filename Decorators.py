# # 1
def my_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@my_decorator
def my_function():
    print("Hello. I am the decorated function")
my_function()

function = my_decorator(my_function)
function()
#
# # 2
def my_decorator(func):
    def wrapper(n):
        print("Start")
        func(n)
        print("End")
    return wrapper

@my_decorator
def my_function(number):
    print(number + 1)

my_function(10)
#
# # 3
# def my_decorator_1(func):
#     def wrapper(n):
#         print("First decorator: start")
#         func(n)
#         print("First decorator: end")
#     return wrapper
#
# def my_decorator_2(func):
#     def wrapper(num):
#         print("Second decorator: start")
#         func(num)
#         print("Second decorator: end")
#     return wrapper
# @my_decorator_1
# @my_decorator_2
# def my_function(number):
#     print(number + 1)
#
# my_function(10)
# my_function = my_decorator_1(my_decorator_2(my_function))

# 4

import time
import tracemalloc
def my_decorator_1(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Total time: ", end_time - start_time)
        return result
    return wrapper

def my_decorator_2(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Used memory: ", tracemalloc.get_tracemalloc_memory())
        return result
    return wrapper
@my_decorator_1
@my_decorator_2
def reverse_word():
    userWord = input("Please Enter Any Word: ")
    reversedWord = userWord[::-1]
    print(reversedWord)

reverse_word()

