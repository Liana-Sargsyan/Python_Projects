# def my_decorator(func):
#     def wrapper(y):
#         print("Start")
#         func(y)
#         print("End")
#     return wrapper
#
# @my_decorator
# def my_function(year):
#     print(f"Happy New {year} Year")
#
# my_function(2023)

# my_function()
#
# my_function_decorated = my_decorator(my_function)
# my_function_decorated()



import time
import tracemalloc
def time_calculation(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Total time: ", end_time - start_time)
        return result
    return wrapper

def memory_usage(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Used memory: ", tracemalloc.get_tracemalloc_memory())
        return result
    return wrapper
@time_calculation
@memory_usage
def reverse_word():
    userWord = input("Please Enter Any Word: ")
    reversedWord = userWord[::-1]
    print(reversedWord)

reverse_word()

