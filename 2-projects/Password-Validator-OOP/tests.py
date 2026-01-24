import unittest
from Password_validator import PasswordValidator


class TestPasswordValidator(unittest.TestCase):
    def test_is_valid(self):
        validator = PasswordValidator("G345678")
        assert validator.is_valid() == False
        validator = PasswordValidator("sG345678")
        assert validator.is_valid() == True
        validator = PasswordValidator("sG345678")
        assert validator.is_valid() == True
        
    def test_has_uppercase(self):
        validator = PasswordValidator("sG345678")
        self.assertTrue(validator.has_uppercase())
        validator = PasswordValidator("sg345678")
        self.assertFalse(validator.has_uppercase())
        
    def test_has_lowercase(self):
        validator = PasswordValidator("sG345678")
        self.assertTrue(validator.has_lowercase())
        validator = PasswordValidator("SG345678")
        self.assertFalse(validator.has_lowercase())
        
    def test_has_digit(self):
        validator = PasswordValidator("sG345678")
        self.assertTrue(validator.has_digit())
        validator = PasswordValidator("sgG")
        self.assertFalse(validator.has_digit())
        
if __name__ == "__main__":
    unittest.main()
