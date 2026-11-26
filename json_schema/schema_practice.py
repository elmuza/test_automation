import json
from pathlib import Path

from jsonschema import validate
from jsonschema.exceptions import SchemaError, ValidationError
from referencing import Registry, Resource


BASE_DIR = Path(__file__).resolve().parent


def load_schema(path):
    schema_path = BASE_DIR / path
    with schema_path.open(encoding="utf-8") as file:
        schema = json.load(file)

    return schema


def validate_data(data, schema, registry=None):
    try:
        if registry is None:
            validate(data, schema)
        else:
            validate(data, schema, registry=registry)
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

product_schema = load_schema(Path("schemas") / "product.json")
products_schema = load_schema(Path("products.json"))
order_schema = load_schema(Path("schemas") / "order.json")

product_registry = Registry().with_resource(
    product_schema["$id"],
    Resource.from_contents(product_schema),
)


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
validate_data(products, products_schema, product_registry)
validate_data(product, product_schema)

