# Expense Tracker CLI (Python)

A terminal-based Expense Tracker where the user can add, view, and delete expenses. All data is stored persistently in a CSV file.

## Features
- Add new expenses with date, description, and amount
- View all recorded expenses
- Delete expenses by index
- Input validation and error handling
- Persistent storage using CSV
- Logging of actions for debugging

## How It Works
- Users interact through a terminal menu.
- Each expense includes:
  - `date` (YYYY-MM-DD)
  - `description`
  - `amount`
- Expenses are stored in `expenses.csv` for persistence.
- Users can view all expenses or delete a specific one by index.

Each action:
- Validates user input
- Updates the CSV file
- Logs the action

## How to Run
Make sure you have Python 3 installed.  

```bash
python main.py
Follow the on-screen menu to add, view, or delete expenses.

CSV Format
The CSV file expenses.csv uses the following columns:

date,description,amount
2026-01-22,Coffee,2.5
Technologies
Python 3

csv module

os module

logging module

Purpose
This project was created to practice:

File handling with CSV

Modular Python programming

CLI design and menu interaction

Input validation and error handling

Logging user actions