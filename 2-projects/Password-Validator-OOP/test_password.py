import pytest

from validators import PasswordValidator

def test_len_password():
    validator = PasswordValidator()
    validator.len_password("12345679")
    assert True
    
def test_has_uppercase():
    validator = PasswordValidator()
    validator.has_uppercase("SSs345679")
    assert True
    
def test_has_lowercase():
    validator = PasswordValidator()
    validator.has_lowercase("sss345679")
    assert True
    
def test_has_digit():
    validator = PasswordValidator()
    validator.has_digit("sss345679")
    assert True

