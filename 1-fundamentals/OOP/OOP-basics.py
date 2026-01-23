
"""Simple Car and BankAccount classes"""
class Car:
    def __init__(self,make,model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def __str__(self):
        return f"{self.make} {self.model} {self.year}"
    
    def __repr__(self):
        return f"Car({self.make}, {self.model}, {self.year})"
    
car = Car("Toyota", "Corolla", 2022)
car.model = "Camry"
print(car)


class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        if amount > self.balance:
            return "No hay fondos suficientes"
        return self.balance
    
    def __str__(self):
        return f"{self.owner} tiene {self.balance} en su cuenta"
    
account = BankAccount("Iriome", 100)
account.deposit(100)
account.withdraw(200)
print(account.balance)
print(account)
