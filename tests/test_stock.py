
from stock_utils import is_valid_stock_id


def test_valid_stock_id():
    assert is_valid_stock_id("2330") is True
    assert is_valid_stock_id("0050") is True
    assert is_valid_stock_id("123456") is True


def test_invalid_stock_id():
    assert is_valid_stock_id("123") is False
    assert is_valid_stock_id("abcdef") is False
    assert is_valid_stock_id("23a0") is False
    assert is_valid_stock_id("") is False
