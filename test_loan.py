import pytest
from loan import monthly_payment


def test_normal_loan():
    assert monthly_payment(10000, 12, 36) == 332.14


def test_zero_interest():
    assert monthly_payment(1200, 0, 12) == 100.00


def test_bad_amount():
    with pytest.raises(ValueError):
        monthly_payment(-500, 10, 12)