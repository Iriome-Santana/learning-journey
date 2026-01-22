import csv
import os
import logging

FILE_NAME = "expenses.csv"

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)
    for expense in expenses:
        expense["amount"] = float(expense["amount"])
        
    return expenses

def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "description", "amount"])
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(expense):
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    
def show_expenses():
    expenses = load_expenses()
    if not expenses:
        raise ValueError("No expenses found")
    for index, expense in enumerate(expenses):
        print(f"{index + 1}. {expense['date']} - {expense['description']} - {expense['amount']}")
    
def delete_expense(expense_index):
    expenses = load_expenses()
    if not expenses:
        raise ValueError("No expenses found")
    if not expense_index.isdigit():
        raise ValueError("Expense index must be a number")
    
    index = int(expense_index) - 1
    
    if index < 0 or index >= len(expenses):
        raise ValueError("Expense not found")
    
    expenses.pop(index)
    save_expenses(expenses)
