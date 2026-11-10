import json
from pathlib import Path

file_path = Path(__file__).parent / "test_data.json"

with file_path.open("r", encoding="utf-8") as file:
    products = json.load(file)

for product in products:
    name = product["name"]
    price = product["price"]
    quantity = product["quantity"]

    total = price * quantity

    print(f"Товар: {name}")
    print(f"Цена: {price}")
    print(f"Количество: {quantity}")
    print(f"Общая стоимость: {total}")
    print("---")