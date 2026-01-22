import csv
import os
import logging
from expenses import *


def menu():
    print("\nMenu:")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Delete expense")
    print("4. Exit")
    option = input("Enter option: ")
    return option

def main():
    while True:
        option = menu()
        try:
            if option == "1":
                date = input("Enter date (YYYY-MM-DD): ")
                description = input("Enter description: ")
                amount = float(input("Enter amount: "))

                expense = {"date": date, "description": description, "amount": str(amount)}

                add_expense(expense)
                print("Expense added successfully!")
                logging.info("Expense added successfully!")

            elif option == "2":
                show_expenses()
                logging.info("User show expenses")

            elif option == "3":
                show_expenses()
                delete_expense(input("Enter expense index: "))
                logging.info("User delete expense")
                print("Expense deleted successfully!")

            elif option == "4":
                logging.info("User exit the program")
                print("See you later!")
                break

            else:
                print("Invalid option")
                logging.warning("User enter a inexistent option")
        except ValueError as e:
            print(e)
        
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()