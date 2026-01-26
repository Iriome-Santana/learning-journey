from storage import load_expenses, save_expenses


class ExpenseManager:
    def __init__(self):
        self.expenses = load_expenses()
    
    def add_expense(self, date: str, description: str, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        expense = {"date": date, "description": description, "amount": amount}
        
        self.expenses.append(expense)
        save_expenses(self.expenses)
    
    def show_expenses(self):
        return self.expenses
    
    def delete_expense(self, index: int):
        if not self.expenses:
            raise ValueError("No expenses to delete")
        if index < 0 or index >= len(self.expenses):
            raise ValueError("Expense not found")
        self.expenses.pop(index)
        save_expenses(self.expenses)
        
    def summary(self):
        total = sum(expense["amount"] for expense in self.expenses)
        return total
