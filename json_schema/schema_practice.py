from jsonschema import validate

product = {
    "id": 10,
    "name": "Monitor",
    "price": 15000,
    "in_stock": True,
}

product_schema = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer",
        },
        "name": {
            "type": "string",
        },
        "price": {
            "type": "integer",
        },
        "in_stock": {
            "type": "boolean",
        },
    },
    "required": ["id", "name", "price", "in_stock"],
}

validate(instance=product, schema=product_schema)

print("Validation passed")
