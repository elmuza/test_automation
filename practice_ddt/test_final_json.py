from pathlib import Path
import json
import pytest

path = Path(__file__).parent/'final_products.json'

with path.open('r', encoding='utf-8') as file:
    items = json.load(file)
    
@pytest.mark.parametrize('product', items)
def test_real_price(product):
    price = product['price']
    quantity = product['quantity']
    expected_total = product['expected_total']
    
    real_price = price*quantity
    
    assert expected_total == real_price


