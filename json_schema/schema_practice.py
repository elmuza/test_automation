from jsonschema import validate
from jsonschema.exceptions import ValidationError, SchemaError
import json
from pathlib import Path

product = {
    "id": 10,
    "name": "Monitor",
    "price": 15000,
    "in_stock": True,
    "manufacturer": {
        "id": 5,
        "name": "Samsung",
        "country": "South Korea",
    },
    "tags": ["electronics", "gaming", "monitor"],
}

BASE_DIR = Path(__file__).resolve().parent

schema_path = BASE_DIR / "schemas" / "product.json"

with schema_path.open(encoding="utf-8") as file:
    product_schema = json.load(file)

products = [
    {
        "id": 10,
        "name": "Monitor",
        "price": 15000,
        "in_stock": True,
        "manufacturer": {
            "id": 5,
            "name": "Samsung",
            "country": "South Korea",
        },
        "tags": ["electronics", "monitor"],
    },
    {
        "id": 11,
        "name": "Keyboard",
        "price": 3500,
        "in_stock": False,
        "manufacturer": {
            "id": 6,
            "name": "Logitech",
            "country": "Switzerland",
        },
        "tags": ["electronics", "gaming"],
    },
]

products_schema = {
    "type": "array",
    "minItems": 0,
    "maxItems": 100,
    "uniqueItems": True,
    "items": product_schema,
}

def validate_data(data, schema):
    try:
        validate(data, schema)
    except ValidationError as error:
        print("Message:", error.message)
        print("Path", list(error.path))
        print("Schema path", list(error.schema_path))
        print("Rule:", error.validator)
        print("Expected:", error.validator_value)
        print("Actual:", error.instance)
        return False
    except SchemaError:
        print("Invalid schema")
        return False
    else:
        print("Validation passed")
        return True
    
validate_data(products, products_schema)
validate_data(product, product_schema)


BASE_DIR = Path(__file__).resolve().parent

schema_path = BASE_DIR / "schemas" / "order.json"

with schema_path.open(encoding="utf-8") as file:
    order_schema = json.load(file)

order = {
    "id": 100,
    "delivery_address": {
        "city": "Bender",
        "street": "Lenina 10",
        "postal_code": "3200",
    },
    "billing_address": {
        "city": "Tiraspol",
        "street": "Mira 15",
        "postal_code": "3300",
    },
}

validate_data(order, order_schema)