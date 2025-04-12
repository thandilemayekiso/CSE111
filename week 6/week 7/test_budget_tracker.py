import pytest
from datetime import datetime
from budget_tracker import calculate_totals, summarize_by_category, get_largest_expense, filter_by_date

sample_transactions = [
    {"date": datetime(2025, 4, 1), "description": "Salary", "category": "Income", "amount": 5000.00},
    {"date": datetime(2025, 4, 2), "description": "Groceries", "category": "Food", "amount": -800.00},
    {"date": datetime(2025, 4, 3), "description": "Electricity", "category": "Utilities", "amount": -600.00}
]

def test_calculate_totals():
    income, expenses, balance = calculate_totals(sample_transactions)
    assert income == 5000.00
    assert expenses == 1400.00
    assert balance == 3600.00

def test_summarize_by_category():
    summary = summarize_by_category(sample_transactions)
    assert summary["Income"] == 5000.00
    assert summary["Food"] == -800.00
    assert summary["Utilities"] == -600.00

def test_get_largest_expense():
    largest = get_largest_expense(sample_transactions)
    assert largest["description"] == "Groceries"
    assert largest["amount"] == -800.00

def test_filter_by_date():
    start = datetime(2025, 4, 2)
    end = datetime(2025, 4, 3)
    filtered = filter_by_date(sample_transactions, start, end)
    assert len(filtered) == 2
