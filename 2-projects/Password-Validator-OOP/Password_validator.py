
class PasswordValidator:
    def __init__(self, password):
        self.password = password
        
    def has_uppercase(self):
        return any(char.isupper() for char in self.password)
    
    def has_lowercase(self):
        return any(char.islower() for char in self.password)
    
    def has_digit(self):
        return any(char.isdigit() for char in self.password)
    
    def is_valid(self):
        return (self.has_uppercase() 
                and self.has_lowercase() 
                and self.has_digit())
    
        
validator = PasswordValidator("12dsdGDG345678")
print(validator.is_valid())
