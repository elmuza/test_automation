import json
from pathlib import Path
import pytest


file_path = Path(__file__).parent / "test_data.json"

with file_path.open("r", encoding="utf-8") as file:
    products = json.load(file)


@pytest.mark.parametrize("product", products)
def test_product_total(product):
    price = product["price"]
    quantity = product["quantity"]

    total = price * quantity

    assert total > 0