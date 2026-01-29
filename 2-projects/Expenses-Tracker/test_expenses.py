import pytest
from unittest.mock import patch
from expenses import ExpenseManager

"""fixture"""

@pytest.fixture
def manager_mock():
    with patch("expenses.load_expenses", return_value=[]), \
         patch("expenses.save_expenses") as mock_save:
        manager = ExpenseManager()
        yield manager


"""add expense tests"""
def test_add_expense_fixture(manager_mock):
    initial_count = len(manager_mock.expenses)
    
    manager_mock.add_expense("2026-01-27", "Coffee", 3.5)
    
    assert len(manager_mock.expenses) == initial_count + 1
    assert manager_mock.expenses[-1]["description"] == "Coffee"
    assert manager_mock.expenses[-1]["amount"] == 3.5
    
def test_add_expense_amount_negative(manager_mock):
    with pytest.raises(ValueError):
        manager_mock.add_expense("2026-01-27", "Coffee", -3.5)
        
def test_add_expense_amount_zero(manager_mock):
    with pytest.raises(ValueError):
        manager_mock.add_expense("2026-01-27", "Coffee", 0)
        
def test_add_expense_empty_fields(manager_mock):
    with pytest.raises(ValueError):
        manager_mock.add_expense("", "", 0)

"""show expenses tests"""
def test_show_expenses_fixture(manager_mock):
    manager_mock.add_expense("2026-01-27", "Coffee", 3.5)
    assert manager_mock.show_expenses() == [{"date": "2026-01-27", "description": "Coffee", "amount": 3.5}]

def test_show_expenses_empty(manager_mock):
    assert manager_mock.show_expenses() == []

"""delete expense tests"""
def test_delete_expense_fixture(manager_mock):
    manager_mock.add_expense("2026-01-27", "Coffee", 3.5)
    manager_mock.delete_expense(0)
    assert len(manager_mock.expenses) == 0

def test_delete_expense_invalid_index(manager_mock):
    with pytest.raises(ValueError):
        manager_mock.delete_expense(0)
        
def test_delete_expense_no_expenses(manager_mock):
    with pytest.raises(ValueError):
        manager_mock.delete_expense(0)
        
"""summary tests"""
def test_summary_fixture(manager_mock):
    manager_mock.add_expense("2026-01-27", "Coffee", 3.5)
    assert manager_mock.summary() == 3.5