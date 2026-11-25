from jsonschema import validate

product = {
    "id": 1,
    "name": "monitor",
    "price": 1501,
    "in_stock": False,
}

product_schema = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer",
            "exclusiveMinimum": 0,
        },
        "name": {
            "type": "string",
            "minLength": 3,
            "maxLength": 50,
        },
        "price": {
            "type": "integer",
            "minimum": 1,
            "maximum": 1000000,
        },
        "in_stock": {
            "type": "boolean",
        },
    },
    "required": ["id", "name", "price", "in_stock"],
}

validate(instance=product, schema=product_schema)

print("Validation passed")
