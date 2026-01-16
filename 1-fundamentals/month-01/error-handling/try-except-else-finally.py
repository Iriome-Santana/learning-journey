
"""""Basic Error Handling in Python using try, except, else, and finally"""""

"""Basic example of try-except"""
try:
    print(10 + '5')
except:
    print('Something went wrong')

    
"""Using else with try-except"""
try:
    result = 10 / 2
except ZeroDivisionError:
    print('You cannot divide by zero')
else:
    print(f'The result is {result}')

    
"""Using finally with try-except"""
try:
    value = 10 / 2
except ZeroDivisionError:
    print('You cannot divide by zero')
else:
    print(f'The result is {value}')
finally:
    print('This block always executes')

    
"""Catching specific exceptions"""

"""Catching ZeroDivisionError"""
try:
    print(10 / 0)
except ZeroDivisionError:
    print('You cannot divide by zero')


"""Catching ValueError"""
try:
    number = int(input('Enter a number: '))
    print(f'You entered: {number}')
except ValueError:
    print('That is not a valid number')


"""Catching FileNotFoundError"""
try:
    file = open('non_existent_file.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print('The file does not exist')
finally:
    print('Execution completed')

    
"""Catching multiple exceptions"""
try:
    user_input = input('Enter a number to divide 100 by: ')
    number = int(user_input)
    result = 100 / number
except ValueError:
    print('That is not a valid number')
except ZeroDivisionError:
    print('You cannot divide by zero')
else:
    print(f'The result is {result}')
finally:
    print('Thank you for using the program')
    
"""Nested try-except blocks"""
try:
    user_input = input('Enter a number to divide 50 by: ')
    number = int(user_input)
    try:
        result = 50 / number
    except ZeroDivisionError:
        print('You cannot divide by zero')
    else:
        print(f'The result is {result}')
except ValueError:
    print('That is not a valid number')
finally:
    print('Program execution finished')

    
"""Generic exception handling"""
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2025 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

    
