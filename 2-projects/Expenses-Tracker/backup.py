import os
import shutil
from datetime import datetime
import logging
from logging_logic import setup_logging

setup_logging("backup.log")

os.makedirs("backups", exist_ok=True)

def backup_expenses(file_name: str = "expenses.csv"):
    if not os.path.exists(file_name):
        logging.warning("No expenses to backup")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    backup_file = f"backups/expenses_{timestamp}.csv"
    shutil.copy(file_name, backup_file)
    
    logging.info(f"Backup created: {backup_file}")
    