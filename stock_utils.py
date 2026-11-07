
def is_valid_stock_id(stock_id):
    """檢查股票代號是否為 4 至 6 位數字"""
    return stock_id.isdigit() and 4 <= len(stock_id) <= 6
