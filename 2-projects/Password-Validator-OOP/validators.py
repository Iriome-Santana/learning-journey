import logging


class PasswordValidator:
    def __init__(self):
        self.errors = []
    
    def len_password(self, password: str):
        logging.info("Validating password length")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

    def has_uppercase(self, password: str):
        logging.info("Validating password uppercase")
        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter")

    def has_lowercase(self, password: str):
        logging.info("Validating password lowercase")
        if not any(char.islower() for char in password):
            raise ValueError("Password must contain at least one lowercase letter")

    def has_digit(self, password: str):
        logging.info("Validating password digit")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit")