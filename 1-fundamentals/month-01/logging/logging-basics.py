import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program started")
try:
    age = int(input("Enter your age: "))
    
    if age < 18:
        print("You are under-age")
        logging.warning("The user is under-age")
    else:
        print("You are adult, welcome")
        logging.info("The user is adult")

except ValueError:
    print("You have to add a number")
    logging.error("The user did not add a numeric value.", exc_info=True)
    
logging.info("Program finished")

