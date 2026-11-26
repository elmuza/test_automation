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

# validate(instance=product, schema=product_schema)

# print("Product validation passed")

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

# validate(instance=products, schema=products_schema)

# print("Products validation passed")

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



# schemas_dir = Path(__file__).parent / "schemas"

# schema_path = schemas_dir / "product.json"
# schema_path.write_text(
#     json.dumps(product_schema, ensure_ascii=False, indent=4) + "\n",
#     encoding="utf-8",
# )