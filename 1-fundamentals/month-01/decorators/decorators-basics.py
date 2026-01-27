
"""decorator sin params"""
def wrapper(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@wrapper
def saludar():
    print("Hola")

saludar()

"""decorator con params"""

def wrapper(func):
    def wrapper(*args, **kwargs):
        print("Before we are about to greet")
        func(*args, **kwargs)
        print("After we have finished greeting")
    return wrapper

@wrapper
def greet(name, age, gender):
    print(f"Hi {name}, you are {age} years old and you are {gender}")

greet("Iriome", 26, "Male")


