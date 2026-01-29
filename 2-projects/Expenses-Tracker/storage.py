import os
import csv


FILE_NAME = "expenses.csv"
FIELDNAMES = ["date", "description", "amount"]

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)
    except OSError as e:
        logging.error(f"Error loading expenses: {e}")
        return []
    for expense in expenses:
        expense["amount"] = float(expense["amount"])
    return expenses

def save_expenses(expenses):
    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(expenses)
    except OSError as e:
        logging.error(f"Error saving expenses: {e}")