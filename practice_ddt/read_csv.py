import csv
from pathlib import Path

file_path = Path(__file__).parent / "products.csv"

with file_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    products = list(reader)

for product in products:
    name = product["name"]
    price = int(product["price"])
    quantity = int(product["quantity"])

    total = price * quantity

    print(f"Товар: {name}")
    print(f"Стоимость: {total}")
    print("---")