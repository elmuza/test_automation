import csv
import pytest
from pathlib import Path

path = Path(__file__).parent / 'final_products.csv'

with path.open('r', encoding='utf-8',newline="") as file:
    reader = csv.DictReader(file)
    items = list(reader)

@pytest.mark.parametrize('product', items)
def test_real_price(product):
    price = int(product['price'])
    quantity = int(product['quantity'])
    expected_total = int(product['expected_total'])
    
    real_price = price*quantity
    
    assert expected_total == real_price
