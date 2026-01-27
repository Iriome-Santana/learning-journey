import logging
from expenses import ExpenseManager
from logging_logic import setup_logging

def menu():
    print("\nMenu:")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Delete expense")
    print("4. Summary")
    print("5. Exit")
    option = input("Enter option: ")
    return option

def main():
    manager = ExpenseManager()
    while True:
        option = menu()
        try:
            if option == "1":
                try:
                    date = input("Enter date (YYYY-MM-DD): ")
                    description = input("Enter description: ")
                    try:
                        amount = float(input("Enter amount: "))
                    except ValueError:
                        print("Invalid amount")
                        continue
                except ValueError:
                    print("Fields are required")
                    continue

                manager.add_expense(date, description, amount)
                print("Expense added successfully!")
                logging.info("Expense added successfully!")

            elif option == "2":
                expenses = manager.show_expenses()
                
                if not expenses:
                    print("No expenses found")
                    continue
                for index, expense in enumerate(expenses, start=1):
                    print(f"{index}. {expense['date']} - {expense['description']} - {expense['amount']}")
                logging.info("User show expenses")

            elif option == "3":
                expenses = manager.show_expenses()
                if not expenses:
                    print("No expenses to delete")
                    continue
                for i, expense in enumerate(expenses, start=1):
                    print(f"{i}. {expense['date']} - {expense['description']} - {expense['amount']}")
                try:
                    index = int(input("Enter expense index: ")) - 1
                except ValueError:
                    print("Invalid index")
                    continue
                manager.delete_expense(index)
                logging.info("User delete expense")
                print("Expense deleted successfully!")

            elif option == "4":
                logging.info("User show summary")
                print("\nSummary:")
                print(manager.summary())

            elif option == "5":
                logging.info("User exit the program")
                print("See you later!")
                break

            else:
                print("Invalid option")
                logging.warning("User enter a inexistent option")
        except ValueError as e:
            print(e)
        
if __name__ == "__main__":
    setup_logging("expenses.log")
    main()