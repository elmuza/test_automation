import csv
from pathlib import Path
import pytest


file_path = Path(__file__).parent / "products.csv"

with file_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    products = list(reader)


@pytest.mark.parametrize("product", products)
def test_product_total_csv(product):
    price = int(product["price"])
    quantity = int(product["quantity"])

    total = price * quantity

    assert total > 0