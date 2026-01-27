from storage import load_expenses, save_expenses
from functools import wraps


def validate_expense(func):
    @wraps(func)
    def wrapper_inner(self, *args, **kwargs):
        date = args[0]
        description = args[1]
        amount = args[2]
        if not date or not description or not amount:
            raise ValueError("All fields are required")
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return func(self, *args, **kwargs)
    return wrapper_inner

class ExpenseManager:
    """Expense manager class"""
    def __init__(self):
        self.expenses = load_expenses()
            
    
    @validate_expense
    def add_expense(self, date: str, description: str, amount: float):
        expense = {"date": date, "description": description, "amount": amount}
        
        self.expenses.append(expense)
        save_expenses(self.expenses)
    
    def show_expenses(self) -> list:
        return self.expenses
    
    """decorator to check if the index is valid"""
    def check_index(func):
        @wraps(func)
        def wrapper_inner(self, index):
            if not self.expenses:
                raise ValueError("No expenses to delete")
            if index < 0 or index >= len(self.expenses):
                raise ValueError("Expense not found")
            func(self, index)
        return wrapper_inner
    
    @check_index
    def delete_expense(self, index: int):
        self.expenses.pop(index)
        save_expenses(self.expenses)

    def summary(self) -> float:
        total = sum(expense["amount"] for expense in self.expenses)
        return total
